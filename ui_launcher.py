# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_launcher.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SheriffLauncher(object):
    def setupUi(self, SheriffLauncher):
        if not SheriffLauncher.objectName():
            SheriffLauncher.setObjectName(u"SheriffLauncher")
        SheriffLauncher.resize(354, 659)
        self.widget = QWidget(SheriffLauncher)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 331, 643))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_sheriff = QLabel(self.widget)
        self.lbl_sheriff.setObjectName(u"lbl_sheriff")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_sheriff.sizePolicy().hasHeightForWidth())
        self.lbl_sheriff.setSizePolicy(sizePolicy)
        self.lbl_sheriff.setMinimumSize(QSize(0, 200))
        self.lbl_sheriff.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_sheriff)

        self.btn_manage = QPushButton(self.widget)
        self.btn_manage.setObjectName(u"btn_manage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_manage.sizePolicy().hasHeightForWidth())
        self.btn_manage.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_manage)

        self.btn_new_show = QPushButton(self.widget)
        self.btn_new_show.setObjectName(u"btn_new_show")
        sizePolicy1.setHeightForWidth(self.btn_new_show.sizePolicy().hasHeightForWidth())
        self.btn_new_show.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_new_show)

        self.btn_new_shot = QPushButton(self.widget)
        self.btn_new_shot.setObjectName(u"btn_new_shot")
        sizePolicy1.setHeightForWidth(self.btn_new_shot.sizePolicy().hasHeightForWidth())
        self.btn_new_shot.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_new_shot)

        self.btn_new_asset = QPushButton(self.widget)
        self.btn_new_asset.setObjectName(u"btn_new_asset")
        sizePolicy1.setHeightForWidth(self.btn_new_asset.sizePolicy().hasHeightForWidth())
        self.btn_new_asset.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_new_asset)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btn_help = QPushButton(self.widget)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy1.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_help)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.btn_exit = QPushButton(self.widget)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.btn_exit)


        self.retranslateUi(SheriffLauncher)

        QMetaObject.connectSlotsByName(SheriffLauncher)
    # setupUi

    def retranslateUi(self, SheriffLauncher):
        SheriffLauncher.setWindowTitle(QCoreApplication.translate("SheriffLauncher", u"Form", None))
        self.lbl_sheriff.setText(QCoreApplication.translate("SheriffLauncher", u"SHERIFF v0.1", None))
        self.btn_manage.setText(QCoreApplication.translate("SheriffLauncher", u"SHOT MANAGEMENT", None))
        self.btn_new_show.setText(QCoreApplication.translate("SheriffLauncher", u"CREATE NEW SHOW", None))
        self.btn_new_shot.setText(QCoreApplication.translate("SheriffLauncher", u"CREATE NEW SHOT/SHOTS", None))
        self.btn_new_asset.setText(QCoreApplication.translate("SheriffLauncher", u"CREATE NEW ASSET", None))
        self.btn_help.setText(QCoreApplication.translate("SheriffLauncher", u"HELP", None))
        self.btn_exit.setText(QCoreApplication.translate("SheriffLauncher", u"EXIT", None))
    # retranslateUi

