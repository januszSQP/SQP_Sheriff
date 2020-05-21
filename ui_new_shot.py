# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_shot.ui'
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

from dragdrop import DragAndDrop


class Ui_DlgNewShot(object):
    def setupUi(self, DlgNewShot):
        if not DlgNewShot.objectName():
            DlgNewShot.setObjectName(u"DlgNewShot")
        DlgNewShot.resize(847, 1419)
        self.btn_create_tables = QPushButton(DlgNewShot)
        self.btn_create_tables.setObjectName(u"btn_create_tables")
        self.btn_create_tables.setGeometry(QRect(660, 730, 141, 81))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_create_tables.sizePolicy().hasHeightForWidth())
        self.btn_create_tables.setSizePolicy(sizePolicy)
        self.btn_create_tables.setStyleSheet(u"background-color: rgb(253, 104, 8);")
        self.btn_create_show = QPushButton(DlgNewShot)
        self.btn_create_show.setObjectName(u"btn_create_show")
        self.btn_create_show.setGeometry(QRect(630, 1320, 171, 81))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_create_show.sizePolicy().hasHeightForWidth())
        self.btn_create_show.setSizePolicy(sizePolicy1)
        self.widget = QWidget(DlgNewShot)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 690, 761, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_5 = QCheckBox(self.widget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_3.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_3.addWidget(self.checkBox_4)

        self.line = QFrame(DlgNewShot)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(40, 660, 761, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(DlgNewShot)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(40, 820, 761, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_9 = QLabel(DlgNewShot)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 10, 284, 38))
        font = QFont()
        font.setPointSize(32)
        self.label_9.setFont(font)
        self.line_2 = QFrame(DlgNewShot)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(40, 40, 761, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.widget1 = QWidget(DlgNewShot)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 70, 761, 581))
        self.DlgNewShotForm = QFormLayout(self.widget1)
        self.DlgNewShotForm.setObjectName(u"DlgNewShotForm")
        self.DlgNewShotForm.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.DlgNewShotForm.setFormAlignment(Qt.AlignCenter)
        self.DlgNewShotForm.setContentsMargins(0, 0, 50, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.DlgNewShotForm.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBox = QComboBox(self.widget1)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(310, 0))

        self.DlgNewShotForm.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DlgNewShotForm.setItem(2, QFormLayout.LabelRole, self.verticalSpacer)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.DlgNewShotForm.setWidget(3, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(310, 0))
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DlgNewShotForm.setWidget(3, QFormLayout.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.DlgNewShotForm.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lbl_drop_here = DragAndDrop()
        self.lbl_drop_here.setObjectName(u"lbl_drop_here")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_drop_here.sizePolicy().hasHeightForWidth())
        self.lbl_drop_here.setSizePolicy(sizePolicy3)
        self.lbl_drop_here.setMinimumSize(QSize(300, 140))
        self.lbl_drop_here.setAcceptDrops(True)
        # self.lbl_drop_here.setStyleSheet(u"color: rgb(218, 16, 5);")
        # self.lbl_drop_here.setFrameShape(QFrame.Box)
        # self.lbl_drop_here.setLineWidth(8)
        # self.lbl_drop_here.setAlignment(Qt.AlignCenter)

        self.DlgNewShotForm.setWidget(4, QFormLayout.FieldRole, self.lbl_drop_here)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.DlgNewShotForm.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edt_resw = QLineEdit(self.widget1)
        self.edt_resw.setObjectName(u"edt_resw")
        sizePolicy2.setHeightForWidth(self.edt_resw.sizePolicy().hasHeightForWidth())
        self.edt_resw.setSizePolicy(sizePolicy2)
        self.edt_resw.setMinimumSize(QSize(100, 0))
        self.edt_resw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.edt_resw)

        self.edt_resh = QLineEdit(self.widget1)
        self.edt_resh.setObjectName(u"edt_resh")

        self.horizontalLayout.addWidget(self.edt_resh)


        self.DlgNewShotForm.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")

        self.DlgNewShotForm.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.edt_resw_2 = QLineEdit(self.widget1)
        self.edt_resw_2.setObjectName(u"edt_resw_2")
        sizePolicy2.setHeightForWidth(self.edt_resw_2.sizePolicy().hasHeightForWidth())
        self.edt_resw_2.setSizePolicy(sizePolicy2)
        self.edt_resw_2.setMinimumSize(QSize(100, 0))
        self.edt_resw_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.edt_resw_2)

        self.edt_resh_2 = QLineEdit(self.widget1)
        self.edt_resh_2.setObjectName(u"edt_resh_2")

        self.horizontalLayout_2.addWidget(self.edt_resh_2)


        self.DlgNewShotForm.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.DlgNewShotForm.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.edt_fps = QLineEdit(self.widget1)
        self.edt_fps.setObjectName(u"edt_fps")
        self.edt_fps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.DlgNewShotForm.setWidget(7, QFormLayout.FieldRole, self.edt_fps)

        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.DlgNewShotForm.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.lst_colorspace = QComboBox(self.widget1)
        self.lst_colorspace.setObjectName(u"lst_colorspace")
        sizePolicy2.setHeightForWidth(self.lst_colorspace.sizePolicy().hasHeightForWidth())
        self.lst_colorspace.setSizePolicy(sizePolicy2)
        self.lst_colorspace.setMinimumSize(QSize(310, 0))

        self.DlgNewShotForm.setWidget(8, QFormLayout.FieldRole, self.lst_colorspace)

        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")

        self.DlgNewShotForm.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.cal_startdate = QCalendarWidget(self.widget1)
        self.cal_startdate.setObjectName(u"cal_startdate")
        sizePolicy3.setHeightForWidth(self.cal_startdate.sizePolicy().hasHeightForWidth())
        self.cal_startdate.setSizePolicy(sizePolicy3)
        self.cal_startdate.setMinimumSize(QSize(0, 0))

        self.DlgNewShotForm.setWidget(9, QFormLayout.FieldRole, self.cal_startdate)

        self.checkBox = QCheckBox(self.widget1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.DlgNewShotForm.setWidget(10, QFormLayout.FieldRole, self.checkBox)

        self.widget2 = QWidget(DlgNewShot)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(40, 850, 761, 461))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout.addWidget(self.label_11)

        self.lst_shotsList = QTableWidget(self.widget2)
        if (self.lst_shotsList.columnCount() < 5):
            self.lst_shotsList.setColumnCount(5)
        if (self.lst_shotsList.rowCount() < 6):
            self.lst_shotsList.setRowCount(6)
        self.lst_shotsList.setObjectName(u"lst_shotsList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lst_shotsList.sizePolicy().hasHeightForWidth())
        self.lst_shotsList.setSizePolicy(sizePolicy4)
        self.lst_shotsList.setFrameShape(QFrame.StyledPanel)
        self.lst_shotsList.setFrameShadow(QFrame.Plain)
        self.lst_shotsList.setDragEnabled(True)
        self.lst_shotsList.setDragDropMode(QAbstractItemView.DragDrop)
        self.lst_shotsList.setAlternatingRowColors(True)
        self.lst_shotsList.setGridStyle(Qt.NoPen)
        self.lst_shotsList.setRowCount(6)
        self.lst_shotsList.setColumnCount(5)
        self.lst_shotsList.horizontalHeader().setMinimumSectionSize(16)

        self.verticalLayout.addWidget(self.lst_shotsList)


        self.retranslateUi(DlgNewShot)

        QMetaObject.connectSlotsByName(DlgNewShot)
    # setupUi

    def retranslateUi(self, DlgNewShot):
        DlgNewShot.setWindowTitle(QCoreApplication.translate("DlgNewShot", u"Dialog", None))
        self.btn_create_tables.setText(QCoreApplication.translate("DlgNewShot", u"add shot", None))
        self.btn_create_show.setText(QCoreApplication.translate("DlgNewShot", u"FINISH", None))
        self.label_4.setText(QCoreApplication.translate("DlgNewShot", u"TASKS :", None))
        self.checkBox_2.setText(QCoreApplication.translate("DlgNewShot", u"COMPOSITING", None))
        self.checkBox_3.setText(QCoreApplication.translate("DlgNewShot", u"3D TRACKING", None))
        self.checkBox_5.setText(QCoreApplication.translate("DlgNewShot", u"3D", None))
        self.checkBox_4.setText(QCoreApplication.translate("DlgNewShot", u"DMP", None))
        self.label_9.setText(QCoreApplication.translate("DlgNewShot", u"CREATE NEW SHOT", None))
        self.label_2.setText(QCoreApplication.translate("DlgNewShot", u"SELECT SHOW : ", None))
        self.label.setText(QCoreApplication.translate("DlgNewShot", u"SHOT NAME :", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("DlgNewShot", u"shot name ...", None))
        self.label_3.setText(QCoreApplication.translate("DlgNewShot", u"THUMBNAIL :", None))
        self.lbl_drop_here.setText(QCoreApplication.translate("DlgNewShot", u"drop the poster image here", None))
        self.label_5.setText(QCoreApplication.translate("DlgNewShot", u"RESOLUTION :", None))
        self.edt_resw.setPlaceholderText(QCoreApplication.translate("DlgNewShot", u"width ...", None))
        self.edt_resh.setPlaceholderText(QCoreApplication.translate("DlgNewShot", u"height ...", None))
        self.label_8.setText(QCoreApplication.translate("DlgNewShot", u"START/END FRAME :", None))
        self.edt_resw_2.setPlaceholderText(QCoreApplication.translate("DlgNewShot", u"start frame ...", None))
        self.edt_resh_2.setPlaceholderText(QCoreApplication.translate("DlgNewShot", u"end frame ...", None))
        self.label_6.setText(QCoreApplication.translate("DlgNewShot", u"FPS :", None))
        self.edt_fps.setPlaceholderText(QCoreApplication.translate("DlgNewShot", u"fps ...", None))
        self.label_7.setText(QCoreApplication.translate("DlgNewShot", u"COLORSPACE :", None))
        self.label_10.setText(QCoreApplication.translate("DlgNewShot", u"START DATE :", None))
        self.checkBox.setText(QCoreApplication.translate("DlgNewShot", u"CREATE NUKE SCRIPT", None))
        self.label_11.setText(QCoreApplication.translate("DlgNewShot", u"SHOTS LIST", None))
    # retranslateUi

