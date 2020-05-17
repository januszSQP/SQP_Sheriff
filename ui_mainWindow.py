# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1042, 791)
        self.vboxLayout = QVBoxLayout(mainWindow)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.tabWidget = QTabWidget(mainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        font = QFont()
        font.setPointSize(13)
        self.tab.setFont(font)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(292, 101, 115, 22))
        font1 = QFont()
        font1.setFamily(u".AppleSystemUIFont")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_title = QLineEdit(self.tab)
        self.txt_title.setObjectName(u"txt_title")
        self.txt_title.setGeometry(QRect(415, 101, 411, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_title.sizePolicy().hasHeightForWidth())
        self.txt_title.setSizePolicy(sizePolicy)
        self.txt_title.setMinimumSize(QSize(125, 20))
        self.txt_title.setBaseSize(QSize(0, 0))
        self.txt_title.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";")
        self.txt_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(338, 133, 69, 22))
        font2 = QFont()
        font2.setPointSize(18)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_short = QLineEdit(self.tab)
        self.txt_short.setObjectName(u"txt_short")
        self.txt_short.setGeometry(QRect(415, 133, 125, 21))
        self.txt_short.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 165, 127, 22))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(286, 247, 121, 22))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_resolutionW = QLineEdit(self.tab)
        self.txt_resolutionW.setObjectName(u"txt_resolutionW")
        self.txt_resolutionW.setGeometry(QRect(415, 247, 125, 21))
        self.txt_resolutionW.setMinimumSize(QSize(125, 0))
        self.txt_resolutionW.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(365, 279, 42, 22))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_fps = QLineEdit(self.tab)
        self.txt_fps.setObjectName(u"txt_fps")
        self.txt_fps.setGeometry(QRect(415, 279, 125, 21))
        self.txt_fps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(294, 343, 113, 22))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cal_startDate = QCalendarWidget(self.tab)
        self.cal_startDate.setObjectName(u"cal_startDate")
        self.cal_startDate.setGeometry(QRect(415, 343, 304, 194))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cal_startDate.sizePolicy().hasHeightForWidth())
        self.cal_startDate.setSizePolicy(sizePolicy1)
        self.cal_startDate.setGridVisible(False)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 721, 61))
        font3 = QFont()
        font3.setPointSize(40)
        self.label_7.setFont(font3)
        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 49, 991, 51))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.txt_resolutionH = QLineEdit(self.tab)
        self.txt_resolutionH.setObjectName(u"txt_resolutionH")
        self.txt_resolutionH.setGeometry(QRect(580, 250, 125, 21))
        self.txt_resolutionH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        # self.drop_poster = QLabel(self.tab)
        # self.drop_poster.setObjectName(u"drop_poster")
        # self.drop_poster.setGeometry(QRect(420, 170, 111, 71))
        # self.drop_poster.setFrameShape(QFrame.Box)


        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 550, 1041, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.chbx_sequences = QCheckBox(self.widget)
        self.chbx_sequences.setObjectName(u"chbx_sequences")
        font4 = QFont()
        font4.setPointSize(15)
        self.chbx_sequences.setFont(font4)

        self.horizontalLayout_2.addWidget(self.chbx_sequences)

        self.chbx_episodes = QCheckBox(self.widget)
        self.chbx_episodes.setObjectName(u"chbx_episodes")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setWeight(50)
        self.chbx_episodes.setFont(font5)

        self.horizontalLayout_2.addWidget(self.chbx_episodes)

        self.chbx_folderStructure = QCheckBox(self.widget)
        self.chbx_folderStructure.setObjectName(u"chbx_folderStructure")
        self.chbx_folderStructure.setFont(font4)
        self.chbx_folderStructure.setChecked(True)

        self.horizontalLayout_2.addWidget(self.chbx_folderStructure)

        self.widget1 = QWidget(self.tab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(570, 620, 431, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
#ifndef Q_OS_MAC
        self.horizontalLayout_3.setSpacing(-1)
#endif
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_cancel = QPushButton(self.widget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.btn_cancel)

        self.btn_createShow = QPushButton(self.widget1)
        self.btn_createShow.setObjectName(u"btn_createShow")
        sizePolicy2.setHeightForWidth(self.btn_createShow.sizePolicy().hasHeightForWidth())
        self.btn_createShow.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.btn_createShow)

        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(283, 311, 124, 22))
        self.label_20.setFont(font2)
        self.txt_colorspace = QLineEdit(self.tab)
        self.txt_colorspace.setObjectName(u"txt_colorspace")
        self.txt_colorspace.setGeometry(QRect(415, 311, 125, 21))
        self.txt_colorspace.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget = QWidget(self.tab_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(19, 79, 531, 651))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.txt_shotName = QLineEdit(self.formLayoutWidget)
        self.txt_shotName.setObjectName(u"txt_shotName")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.txt_shotName)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.txt_thumbnail = QLineEdit(self.formLayoutWidget)
        self.txt_thumbnail.setObjectName(u"txt_thumbnail")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.txt_thumbnail)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.txt_shotResolution = QLineEdit(self.formLayoutWidget)
        self.txt_shotResolution.setObjectName(u"txt_shotResolution")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.txt_shotResolution)

        self.label_12 = QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.txt_shotFps = QLineEdit(self.formLayoutWidget)
        self.txt_shotFps.setObjectName(u"txt_shotFps")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.txt_shotFps)

        self.label_13 = QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.txt_shotStartFrame = QLineEdit(self.formLayoutWidget)
        self.txt_shotStartFrame.setObjectName(u"txt_shotStartFrame")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.txt_shotStartFrame)

        self.label_14 = QLabel(self.formLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_14)

        self.txt_shotEndFrame = QLineEdit(self.formLayoutWidget)
        self.txt_shotEndFrame.setObjectName(u"txt_shotEndFrame")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.txt_shotEndFrame)

        self.label_15 = QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_15)

        self.txt_shotColorspace = QLineEdit(self.formLayoutWidget)
        self.txt_shotColorspace.setObjectName(u"txt_shotColorspace")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.txt_shotColorspace)

        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.txt_shotLutPath = QLineEdit(self.formLayoutWidget)
        self.txt_shotLutPath.setObjectName(u"txt_shotLutPath")

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.txt_shotLutPath)

        self.label_17 = QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.label_17)

        self.txt_shotCamPath = QLineEdit(self.formLayoutWidget)
        self.txt_shotCamPath.setObjectName(u"txt_shotCamPath")

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.txt_shotCamPath)

        self.label_18 = QLabel(self.formLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.label_18)

        self.txt_shotLensDist = QLineEdit(self.formLayoutWidget)
        self.txt_shotLensDist.setObjectName(u"txt_shotLensDist")

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.txt_shotLensDist)

        self.label_19 = QLabel(self.formLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_5.setWidget(10, QFormLayout.LabelRole, self.label_19)

        self.cal_shotStartDate = QCalendarWidget(self.formLayoutWidget)
        self.cal_shotStartDate.setObjectName(u"cal_shotStartDate")

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.cal_shotStartDate)

        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(589, 79, 391, 521))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.show_treeView = QTreeView(self.horizontalLayoutWidget)
        self.show_treeView.setObjectName(u"show_treeView")

        self.horizontalLayout_5.addWidget(self.show_treeView)

        self.horizontalLayoutWidget_2 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(549, 639, 431, 91))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(40, 0, 0, 0)
        self.btn_shotCancel = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_shotCancel.setObjectName(u"btn_shotCancel")
        sizePolicy2.setHeightForWidth(self.btn_shotCancel.sizePolicy().hasHeightForWidth())
        self.btn_shotCancel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.btn_shotCancel)

        self.btn_shotCreate = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_shotCreate.setObjectName(u"btn_shotCreate")
        sizePolicy2.setHeightForWidth(self.btn_shotCreate.sizePolicy().hasHeightForWidth())
        self.btn_shotCreate.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.btn_shotCreate)

        self.widget2 = QWidget(self.tab_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 10, 961, 54))
        self.horizontalLayout_4 = QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.lst_projChooser = QComboBox(self.widget2)
        self.lst_projChooser.setObjectName(u"lst_projChooser")

        self.horizontalLayout_4.addWidget(self.lst_projChooser)

        self.tabWidget.addTab(self.tab_2, "")

        self.vboxLayout.addWidget(self.tabWidget)

        QWidget.setTabOrder(self.txt_title, self.txt_short)
        QWidget.setTabOrder(self.txt_short, self.txt_resolutionW)
        QWidget.setTabOrder(self.txt_resolutionW, self.txt_resolutionH)
        QWidget.setTabOrder(self.txt_resolutionH, self.txt_fps)
        QWidget.setTabOrder(self.txt_fps, self.txt_colorspace)
        QWidget.setTabOrder(self.txt_colorspace, self.cal_startDate)
        QWidget.setTabOrder(self.cal_startDate, self.btn_createShow)
        QWidget.setTabOrder(self.btn_createShow, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.chbx_sequences)
        QWidget.setTabOrder(self.chbx_sequences, self.chbx_episodes)
        QWidget.setTabOrder(self.chbx_episodes, self.chbx_folderStructure)
        QWidget.setTabOrder(self.chbx_folderStructure, self.txt_thumbnail)
        QWidget.setTabOrder(self.txt_thumbnail, self.txt_shotResolution)
        QWidget.setTabOrder(self.txt_shotResolution, self.txt_shotFps)
        QWidget.setTabOrder(self.txt_shotFps, self.txt_shotStartFrame)
        QWidget.setTabOrder(self.txt_shotStartFrame, self.txt_shotEndFrame)
        QWidget.setTabOrder(self.txt_shotEndFrame, self.txt_shotColorspace)
        QWidget.setTabOrder(self.txt_shotColorspace, self.txt_shotLutPath)
        QWidget.setTabOrder(self.txt_shotLutPath, self.txt_shotCamPath)
        QWidget.setTabOrder(self.txt_shotCamPath, self.txt_shotLensDist)
        QWidget.setTabOrder(self.txt_shotLensDist, self.cal_shotStartDate)
        QWidget.setTabOrder(self.cal_shotStartDate, self.show_treeView)
        QWidget.setTabOrder(self.show_treeView, self.btn_shotCreate)
        QWidget.setTabOrder(self.btn_shotCreate, self.btn_shotCancel)
        QWidget.setTabOrder(self.btn_shotCancel, self.lst_projChooser)
        QWidget.setTabOrder(self.lst_projChooser, self.txt_shotName)
        QWidget.setTabOrder(self.txt_shotName, self.tabWidget)

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"SHOW TITLE :", None))
        self.txt_title.setPlaceholderText(QCoreApplication.translate("mainWindow", u"enter the title", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"SHORT :", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"POSTER PATH :", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"RESOLUTION :", None))
        self.txt_resolutionW.setInputMask("")
        self.txt_resolutionW.setText("")
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"FPS :", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"START DATE :", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"CREATE NEW SHOW", None))
        # self.drop_poster.setText(QCoreApplication.translate("mainWindow", u"drop your image here", None))
        self.chbx_sequences.setText(QCoreApplication.translate("mainWindow", u"SPLIT FOR SEQUENCES", None))
        self.chbx_episodes.setText(QCoreApplication.translate("mainWindow", u"SPLIT FOR EPISODES", None))
        self.chbx_folderStructure.setText(QCoreApplication.translate("mainWindow", u"CREATE FOLDER STRUCTURE", None))
        self.btn_cancel.setText(QCoreApplication.translate("mainWindow", u"CANCEL", None))
        self.btn_createShow.setText(QCoreApplication.translate("mainWindow", u"CREATE SHOW", None))
        self.label_20.setText(QCoreApplication.translate("mainWindow", u"COLORSPACE :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"NEW SHOW", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"SHOT NAME :", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"SHOT THUMBNAIL :", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"RESOLUTION :", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"FPS :", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"START FRAME :", None))
        self.label_14.setText(QCoreApplication.translate("mainWindow", u"END FRAME :", None))
        self.label_15.setText(QCoreApplication.translate("mainWindow", u"COLORSPACE :", None))
        self.label_16.setText(QCoreApplication.translate("mainWindow", u"LUT PATH :", None))
        self.label_17.setText(QCoreApplication.translate("mainWindow", u"3D CAMERA PATH :", None))
        self.label_18.setText(QCoreApplication.translate("mainWindow", u"LENS DISTORTION STMAP PATH :", None))
        self.label_19.setText(QCoreApplication.translate("mainWindow", u"START DATE :", None))
        self.btn_shotCancel.setText(QCoreApplication.translate("mainWindow", u"CANCEL", None))
        self.btn_shotCreate.setText(QCoreApplication.translate("mainWindow", u"CREATE NEW SHOT", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"CREATE NEW SHOT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"NEW SHOT", None))
    # retranslateUi

