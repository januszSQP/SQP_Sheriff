import os, sys, platform
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import sqlalchemy
import mysql.connector
from PIL import Image

'''
    Modules for Clickup connections
'''
import urllib.request
import certifi
import ssl
import json
from pathlib import Path
import yaml
import pickle

import qdarkgraystyle

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import base
from ui_launcher import Ui_SheriffLauncher
from ui_new_show import Ui_DlgNewShow


'''
Class and methods for creating a new show, assign poster (by drag & drop),
creating space in Clickup (if chosen) and creating project for reviews
in SyncSketch (if chosen).
'''
class WindowShow(QDialog, Ui_DlgNewShow):
    def __init__(self):

        super(WindowShow, self).__init__()
        # self.setAcceptDrops(True)
        self.setupUi(self)

        self.btn_cancel.clicked.connect(self.close)
        self.btn_create_show.clicked.connect(self.createNewShow)
        self.btn_create_tables.clicked.connect(self.createTables)


        self.poster_path = ''

    def jobsDir(self):
        Win_Dir = 'J:/'
        Mac_Dir = '/Volumes/mutha/jobs'
        Linux_Dir = '/mnt/jobs'
        # Automatically set global directory
        if platform.system() == "Windows":
            dir = Win_Dir
        elif platform.system() == "Darwin":
            dir = Mac_Dir
        elif platform.system() == "Linux":
            dir = Linux_Dir
        else:
            dir = None
        return dir

    def walk(self, folderDict, path):
        paths = []
        # we only continue if the value is not None
        if folderDict:
            for folder, subDict in folderDict.items():
                # making sure the path will have forward slashes
                # especially necessary on windows
                pathTemp = os.path.normpath(os.path.join(path, folder))
                pathTemp = pathTemp.replace("\\", "/")
                # add the current found path to the list
                paths.append(pathTemp)
                # we call the the function again to go deeper
                # in the dictionary
                paths.extend(self.walk(subDict, pathTemp))
        return paths

    def constructFoldersFromYMLTemplate(self, show, YMLFoldersTemplate):
        # opening the previously saved json file
        # this is to simulate opening a real config file
        folders = {}
        with open(YMLFoldersTemplate, 'r') as f:
            folders = yaml.load(f, Loader=yaml.FullLoader)
        rootPath = self.jobsDir() + '/' + show
        folderPaths = self.walk(folders, rootPath)
        return folderPaths

    def createFolders(self, list):
        for folder in list:
            os.makedirs(folder)

    def createNewShow(self):

        ### Fill th colorspace listbox
        show_title = self.edt_title.text().upper()
        show_title = show_title.replace(' ', '_')
        show_short = self.edt_short.text().upper()
        orig_poster = self.lbl_drop_here.returnImagePath()

        show_resolution = self.edt_resw.text() + 'x' + self.edt_resh.text()
        show_fps = self.edt_fps.text()
        show_colorspace = 'ACES'
        show_startdate = self.cal_startdate.selectedDate().toString(Qt.DefaultLocaleShortDate).split('/')

        ### Create folders
        if self.chk_create_folders.isChecked():
            path_to_config = Path(__file__).parent / "main_folders.yml"
            folders = self.constructFoldersFromYMLTemplate(show_title, path_to_config)
            self.createFolders(folders)

        ### Create Clickup Session
        if self.chk_clickup_space.isChecked():
            print('Connecting to Clickup')
            path_config = Path(__file__).parent / "clickup_api.json"
            path_clickup_space_template = Path(__file__).parent / "clickup_space_template.pckl"
            path_clickup_shots_list_template = Path(__file__).parent / "clickup_shots_list_template.pckl"

            with open(path_config, 'r') as f:
                clickup_api = json.load(f)


            headers = {
                'Authorization': clickup_api.get('API_KEY'),
                'Content-Type': 'application/json'
            }

            '''
            Based on SHOW:title field change the template reading frm .pickle file
            to update xxxxx (stored there) to the proper title.
            Update the url to point to the Workspace.
            Encode the multistring variable stored in .pickle to byte-string format (utf-8),
            required by Clickup API and POST to create the Space (=Show).
            Get the space_id to be written to database and for creating "folderless"
            list in Clickup.
            Read the multistring variable from .pickle file (for list).
            Encode to utf-8.
            POST to create folderless list SHOTS (same will be for ASSETS -> replace SHOTS for ASSETS in variable?).
            Get the list_id to store in database.s
            '''
            f = open(path_clickup_space_template, 'rb')
            clickup_space = pickle.load(f)
            f.close()
            clickup_space = clickup_space.replace('xxxxx', show_title)
            url = 'https://api.clickup.com/api/v2/team/{}/space'.format(clickup_api.get('JOBS_ID'))
            clickup_space = clickup_space.encode('utf-8')
            request = urllib.request.Request(url, data=clickup_space, headers=headers)
            response_body = urllib.request.urlopen(request, context=ssl.create_default_context(cafile=certifi.where())).read()
            response_dict = json.loads(response_body)

            space_id = response_dict.get('id')

            f = open(path_clickup_shots_list_template, 'rb')
            clickup_shots_list = pickle.load(f)
            f.close()
            url = 'https://api.clickup.com/api/v2/space/{}/list'.format(space_id)

            clickup_shots_list = clickup_shots_list.encode('utf-8')
            request = urllib.request.Request(url, data=clickup_shots_list, headers=headers)
            response_body = urllib.request.urlopen(request, context=ssl.create_default_context(cafile=certifi.where())).read()
            response_dict = json.loads(response_body)

            list_id = response_dict.get('id')
        else:
            space_id = ''
            list_id = ''
        ### Create SyncSketch project

        ### Save poster image to <SHOW>/_elements/thumbnails with a name poster.png (convert to .png if needed

        show_poster = self.jobsDir() + '/' + show_title + '/_elements/thumbnails/poster.png'
        img = Image.open(orig_poster)
        size_256 = (256, 256)
        img.thumbnail(size_256)
        img.save(show_poster)

        ### Update database
        new_show = base.Show(title=show_title, short=show_short, poster=show_poster, resolution=show_resolution,
                             fps=show_fps, colorspace=show_colorspace,
                             start_date=date(int(show_startdate[2]), int(show_startdate[1]), int(show_startdate[0])),
                             clickup_space_id=str(space_id), clickup_shot_list_id=str(list_id), clickup_asset_list_id ='')
        #
        base.db.session.add(new_show)
        base.db.session.commit()

        self.close()





    '''
    Temporary function for creating Tables for database.
    ---------------------------------------------------
    Development mode.
    '''
    def createTables(self):
        base.db.create_all()


class MainWindow(QWidget, Ui_SheriffLauncher):
    def __init__(self):

        super(MainWindow, self).__init__()
        # self.setAcceptDrops(True)
        self.setupUi(self)

        ### INITIALIZE GLOBAL VARIABLES FOR PATH RESTORE
        self.PROJ = ''
        self.SEQ = ''
        self.SHOT = ''

        if platform == "linux" or platform == "linux2":
        # linux
            self.ROOT = '/mnt/jobs/'
        elif platform == "darwin":
        # OS X
            self.ROOT = '/Volumes/mutha/jobs/'
        elif platform == "win32":
        # Windows...
            self.ROOT = 'J:/'

        self.date = ''

        ### Launching different
        ### çreate New Show
        # self.btn_getProjects.clicked.connect(self.getProjects)
        # self.cmb_projectList.currentIndexChanged.connect(self.indexChanged)
        # self.cmb_sequenceList.currentIndexChanged.connect(self.getShots)
        # self.lst_shotsList.currentItemChanged.connect(self.getShotPath)
        # self.btn_Temp.clicked.connect(self.createClickupSpace)
        # self.cal_startDate.clicked[QDate].connect(self.getDate)
        self.btn_exit.clicked.connect(QApplication.quit)
        self.btn_new_show.clicked.connect(self.new_show)
        # self.btn_createShow.clicked.connect(self.createNewShow)
        # self.btn_createTables.clicked.connect(self.createTables)


    def new_show(self):
        self.dlg = WindowShow()
        self.dlg.exec_()










# def TestList():
#     show = base.Show.query.filter(base.Show.title == current_show).first()
#     res = show.resolution
#     fps = show.fps
#     #
#     # new_shot = Shot(name='0020', resolution = res, fps = fps, start_frame = '1001', end_frame = '1075',
#     #                 clickup_task_id = '54n2c2', clickup_list_id = '19408057', show_id=show.id)
#     # #
#     shots = base.Shot.query.filter(base.Shot.show_id == show.id)
#     for shot in shots:
#         print(shot.name)
#
#     return "Please list"

# lst = TestList()
#
# print(lst)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    # setup stylesheet
    # app.setStyleSheet(qdarkgraystyle.load_stylesheet())

    mainWin.show()
    ret = app.exec_()
    sys.exit(ret)