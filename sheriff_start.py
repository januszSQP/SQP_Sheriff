import os, sys, platform
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import sqlalchemy
import mysql.connector

import qdarkgraystyle

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui_mainWindow import Ui_mainWindow
import base

from dragdrop import DragAndDrop

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
        self.setupUi(self)

        self.btn_cancel.clicked.connect(self.close)
        self.btn_create_show(self.createNewShow)
        self.btn_create_tables(self.createTables)

    def createNewShow(self):
        print('Create New Show')
        show_title = self.txt_title.text().upper()
        show_short = self.txt_short.text().upper()
        # show_poster = self.txt_poster.text()
        show_resolution = self.txt_resolutionW.text() + 'x' + self.txt_resolutionH.text()
        show_fps = self.txt_fps.text()
        show_colorspace = self.txt_colorspace.text()
        show_startdate = self.cal_startDate.selectedDate().toString(Qt.DefaultLocaleShortDate).split('/')

        new_show = base.Show(title=show_title, short=show_short, poster=show_poster, resolution=show_resolution,
                             fps=show_fps, colorspace=show_colorspace,
                             start_date=date(int(show_startdate[2]), int(show_startdate[1]), int(show_startdate[0])),
                             clickup_space_id='2597557')
        #
        base.db.session.add(new_show)
        base.db.session.commit()

        # print(new_show.title, '   ', new_show.start_date, '   ', len(show_poster))

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
        self.btn_new_show.clicked.connect(self.new_show)
        # self.btn_createShow.clicked.connect(self.createNewShow)
        # self.btn_createTables.clicked.connect(self.createTables)


    def new_show(self):
        self.dlg = WindowShow()
        self.dlg.exec_()
    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasImage:
    #         event.accept()
    #     else:
    #         event.ignore()
    #
    # def dragMoveEvent(self, event):
    #     if event.mimeData().hasImage:
    #         event.accept()
    #     else:
    #         event.ignore()
    #
    # def dragLeaveEvent(self, event):
    #     if event.mimeData().hasImage():
    #         event.setDropAction(Qt.CopyAction)
    #         file_path = event.mimeData().urls()[0].toLocalFile()
    #         self.setImage(file_path)
    #         event.accept()
    #     else:
    #         event.ignore()
    #
    # def setPixmap(self, image):
    #     super().setPixmap(image)

    def setImage(self, file_path):
        print(file_path)
        # image = QPixmap(file_path).scaledToHeight(180, Qt.SmoothTransformation)
        # self.drop_poster.setPixmap(image)

    def MakeDatabaseConnection(self):
        app = Flask(__name__)
        app.config.from_pyfile('config.cfg')

    # def getDate(self):
    #     self.date = self.cal_startDate.selectedDate().toString(Qt.DefaultLocaleShortDate)
    #     return self.date


    '''
    Temporary function for creating Tables for database.
    ---------------------------------------------------
    Development mode.
    '''






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