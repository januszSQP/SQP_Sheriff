import os, sys, platform
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import sqlalchemy
import mysql.connector
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui_mainWindow import Ui_mainWindow
import base

current_show = 'SKYSCRAPER_TEASER'




class MainWindow(QWidget, Ui_mainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
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
        ### çreate New Show
        # self.btn_getProjects.clicked.connect(self.getProjects)
        # self.cmb_projectList.currentIndexChanged.connect(self.indexChanged)
        # self.cmb_sequenceList.currentIndexChanged.connect(self.getShots)
        # self.lst_shotsList.currentItemChanged.connect(self.getShotPath)
        # self.btn_Temp.clicked.connect(self.createClickupSpace)
        # self.cal_startDate.clicked[QDate].connect(self.getDate)
        self.btn_createShow.clicked.connect(self.createNewShow)



    def MakeDatabaseConnection(self):
        app = Flask(__name__)
        app.config.from_pyfile('config.cfg')

    # def getDate(self):
    #     self.date = self.cal_startDate.selectedDate().toString(Qt.DefaultLocaleShortDate)
    #     return self.date

    def createNewShow(self):

        print('Create New Show')
        show_title = self.txt_title.text().upper()
        show_short = self.txt_short.text().upper()
        show_poster = self.txt_poster.text()
        show_resolution = self.txt_resolutionW.text() + 'x' + self.txt_resolutionH.text()
        show_fps = self.txt_fps.text()
        show_colorspace = self.txt_colorspace.text()
        show_startdate = self.cal_startDate.selectedDate().toString(Qt.DefaultLocaleShortDate).split('/')

        new_show = base.Show(title=show_title, short=show_short, poster=show_poster, resolution=show_resolution, fps=show_fps, colorspace=show_colorspace,
                         start_date=date(int(show_startdate[2]), int(show_startdate[1]), int(show_startdate[0])), clickup_space_id='2597557')
        #
        base.db.session.add(new_show)
        base.db.session.commit()

        print(new_show.title, '   ', new_show.start_date, '   ', len(show_poster))

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
    mainWin.show()
    ret = app.exec_()
    sys.exit(ret)