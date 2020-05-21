import sys,os, platform
import json
from pathlib import Path
import yaml
import pickle
from simpledate import SimpleDate
from datetime import date, time

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MainWindow(QWidget):
    def __init__(self):

        super(MainWindow, self).__init__()
        # self.setAcceptDrops(True)
        self.btn_read_date = QPushButton('Read Date')

        self.calendar = QCalendarWidget(self)
        self.calendar.move(20, 20)
        self.calendar.setGridVisible(True)


        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.btn_read_date)

        self.setLayout(layout)

        self.calendar.clicked.connect(self.printDateInfo)

    def printDateInfo(self, qDate):
        print('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
        print('Short date: {}'.format(qDate.toString(Qt.DefaultLocaleShortDate)))
        print('Long date: {}'.format(qDate.toString(Qt.DefaultLocaleLongDate)))
        print('ISO Date: {}'.format(qDate.toString(Qt.ISODate)))

        print(SimpleDate(date=date(qDate.year(), qDate.month(), qDate.day()), time=time(19, 30, 59, 299000), tz='utc').timestamp)
        print(SimpleDate('2020-05-30 19:30:59.299', format='Y-m-d H:M(:S)?', tz='utc').timestamp)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    # setup stylesheet
    # app.setStyleSheet(qdarkgraystyle.load_stylesheet())

    mainWin.show()
    ret = app.exec_()
    sys.exit(ret)