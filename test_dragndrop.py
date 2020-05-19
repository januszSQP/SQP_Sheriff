from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import sys, os, platform

from ui_launcher import Ui_SheriffLauncher
from ui_new_show import Ui_DlgNewShow

class WindowShow(QDialog):

    def __init__(self, *args, **kwargs):
        super(WindowShow, self).__init__(*args, **kwargs)

        self.ui = Ui_DlgNewShow()
        self.ui.setupUi(self)

        # self.ui.btn_cancel.clicked.connect(self.close)

        # self.setupUi(self)
        #
        # self.setWindowTitle("HELLO!")
        #
        # QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        #
        # self.buttonBox = QDialogButtonBox(QBtn)

        # self.buttonBox.rejected.connect(self.reject)
        #
        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.buttonBox)
        # self.setLayout(self.layout)

    def close(self):
        self.close()




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "First Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("New Show", self)
        self.pushButton.move(275, 200)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")

        self.pushButton.clicked.connect(self.window_show)              # <===

        self.main_window()

    def main_window(self):
        self.label = QLabel("Manager", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window_show(self, s):
        print("click", s)
        self.dlg = WindowShow(self)



        self.dlg.exec_()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()
    ret = app.exec_()
    sys.exit(ret)