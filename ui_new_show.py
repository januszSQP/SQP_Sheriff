# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_show.ui'
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


class Ui_DlgNewShow(object):
    def setupUi(self, DlgNewShow):
        if not DlgNewShow.objectName():
            DlgNewShow.setObjectName(u"DlgNewShow")
        DlgNewShow.resize(613, 890)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DlgNewShow.sizePolicy().hasHeightForWidth())
        DlgNewShow.setSizePolicy(sizePolicy)
        DlgNewShow.setModal(True)
        self.label_9 = QLabel(DlgNewShow)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 20, 301, 31))
        font = QFont()
        font.setPointSize(32)
        self.label_9.setFont(font)
        self.btn_create_tables = QPushButton(DlgNewShow)
        self.btn_create_tables.setObjectName(u"btn_create_tables")
        self.btn_create_tables.setGeometry(QRect(30, 780, 141, 81))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_create_tables.sizePolicy().hasHeightForWidth())
        self.btn_create_tables.setSizePolicy(sizePolicy1)
        self.btn_create_tables.setStyleSheet(u"background-color: rgb(253, 104, 8);")
        self.layoutWidget = QWidget(DlgNewShow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 90, 561, 501))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.edt_title = QLineEdit(self.layoutWidget)
        self.edt_title.setObjectName(u"edt_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edt_title.sizePolicy().hasHeightForWidth())
        self.edt_title.setSizePolicy(sizePolicy2)
        self.edt_title.setMinimumSize(QSize(310, 0))
        self.edt_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edt_title)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.edt_short = QLineEdit(self.layoutWidget)
        self.edt_short.setObjectName(u"edt_short")
        sizePolicy2.setHeightForWidth(self.edt_short.sizePolicy().hasHeightForWidth())
        self.edt_short.setSizePolicy(sizePolicy2)
        self.edt_short.setMinimumSize(QSize(100, 0))
        self.edt_short.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edt_short)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)


        ###  DRAG AND DROP
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

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lbl_drop_here)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edt_resw = QLineEdit(self.layoutWidget)
        self.edt_resw.setObjectName(u"edt_resw")
        sizePolicy2.setHeightForWidth(self.edt_resw.sizePolicy().hasHeightForWidth())
        self.edt_resw.setSizePolicy(sizePolicy2)
        self.edt_resw.setMinimumSize(QSize(100, 0))
        self.edt_resw.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.edt_resw)

        self.edt_resh = QLineEdit(self.layoutWidget)
        self.edt_resh.setObjectName(u"edt_resh")

        self.horizontalLayout.addWidget(self.edt_resh)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.edt_fps = QLineEdit(self.layoutWidget)
        self.edt_fps.setObjectName(u"edt_fps")
        self.edt_fps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.edt_fps)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.lst_colorspace = QComboBox(self.layoutWidget)
        self.lst_colorspace.setObjectName(u"lst_colorspace")
        sizePolicy2.setHeightForWidth(self.lst_colorspace.sizePolicy().hasHeightForWidth())
        self.lst_colorspace.setSizePolicy(sizePolicy2)
        self.lst_colorspace.setMinimumSize(QSize(310, 0))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lst_colorspace)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.cal_startdate = QCalendarWidget(self.layoutWidget)
        self.cal_startdate.setObjectName(u"cal_startdate")
        sizePolicy3.setHeightForWidth(self.cal_startdate.sizePolicy().hasHeightForWidth())
        self.cal_startdate.setSizePolicy(sizePolicy3)
        self.cal_startdate.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cal_startdate)

        self.layoutWidget_2 = QWidget(DlgNewShow)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(100, 700, 441, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chk_clickup_space = QCheckBox(self.layoutWidget_2)
        self.chk_clickup_space.setObjectName(u"chk_clickup_space")
        self.chk_clickup_space.setChecked(True)

        self.horizontalLayout_4.addWidget(self.chk_clickup_space)

        self.chk_syncsketch = QCheckBox(self.layoutWidget_2)
        self.chk_syncsketch.setObjectName(u"chk_syncsketch")
        self.chk_syncsketch.setChecked(True)

        self.horizontalLayout_4.addWidget(self.chk_syncsketch)

        self.line_3 = QFrame(DlgNewShow)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 670, 561, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(DlgNewShow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 600, 561, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.layoutWidget_3 = QWidget(DlgNewShow)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(40, 630, 551, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chk_episodes = QCheckBox(self.layoutWidget_3)
        self.chk_episodes.setObjectName(u"chk_episodes")

        self.horizontalLayout_2.addWidget(self.chk_episodes)

        self.chk_sequences = QCheckBox(self.layoutWidget_3)
        self.chk_sequences.setObjectName(u"chk_sequences")

        self.horizontalLayout_2.addWidget(self.chk_sequences)

        self.chk_create_folders = QCheckBox(self.layoutWidget_3)
        self.chk_create_folders.setObjectName(u"chk_create_folders")
        self.chk_create_folders.setChecked(True)

        self.horizontalLayout_2.addWidget(self.chk_create_folders)

        self.line = QFrame(DlgNewShow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 50, 561, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layoutWidget_4 = QWidget(DlgNewShow)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(250, 780, 341, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_cancel = QPushButton(self.layoutWidget_4)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.btn_cancel)

        self.btn_create_show = QPushButton(self.layoutWidget_4)
        self.btn_create_show.setObjectName(u"btn_create_show")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_create_show.sizePolicy().hasHeightForWidth())
        self.btn_create_show.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.btn_create_show)


        self.retranslateUi(DlgNewShow)

        QMetaObject.connectSlotsByName(DlgNewShow)
    # setupUi

    def retranslateUi(self, DlgNewShow):
        DlgNewShow.setWindowTitle(QCoreApplication.translate("DlgNewShow", u"Dialog", None))
        self.label_9.setText(QCoreApplication.translate("DlgNewShow", u"CREATE NEW SHOW", None))
        self.btn_create_tables.setText(QCoreApplication.translate("DlgNewShow", u"CREATE TABLES", None))
        self.label.setText(QCoreApplication.translate("DlgNewShow", u"SHOW TITLE :", None))
        self.edt_title.setPlaceholderText(QCoreApplication.translate("DlgNewShow", u"enter show title ...", None))
        self.label_2.setText(QCoreApplication.translate("DlgNewShow", u"SHORT :", None))
        self.edt_short.setPlaceholderText(QCoreApplication.translate("DlgNewShow", u"enter show short ...", None))
        self.label_3.setText(QCoreApplication.translate("DlgNewShow", u"POSTER PATH :", None))
        self.lbl_drop_here.setText(QCoreApplication.translate("DlgNewShow", u"drop the poster image here", None))
        self.label_5.setText(QCoreApplication.translate("DlgNewShow", u"RESOLUTION :", None))
        self.edt_resw.setPlaceholderText(QCoreApplication.translate("DlgNewShow", u"width ...", None))
        self.edt_resh.setPlaceholderText(QCoreApplication.translate("DlgNewShow", u"height ...", None))
        self.label_6.setText(QCoreApplication.translate("DlgNewShow", u"FPS :", None))
        self.edt_fps.setPlaceholderText(QCoreApplication.translate("DlgNewShow", u"fps ...", None))
        self.label_7.setText(QCoreApplication.translate("DlgNewShow", u"COLORSPACE :", None))
        self.label_8.setText(QCoreApplication.translate("DlgNewShow", u"START DATE :", None))
        self.chk_clickup_space.setText(QCoreApplication.translate("DlgNewShow", u"CREATE CLICKUP SPACE", None))
        self.chk_syncsketch.setText(QCoreApplication.translate("DlgNewShow", u"CREATE SYNCSKETCH LINK", None))
        self.chk_episodes.setText(QCoreApplication.translate("DlgNewShow", u"HAS EPISODES", None))
        self.chk_sequences.setText(QCoreApplication.translate("DlgNewShow", u"HAS SEQUENCES", None))
        self.chk_create_folders.setText(QCoreApplication.translate("DlgNewShow", u"CREATE FOLDERS", None))
        self.btn_cancel.setText(QCoreApplication.translate("DlgNewShow", u"CANCEL", None))
        self.btn_create_show.setText(QCoreApplication.translate("DlgNewShow", u"CREATE NEW SHOW", None))
    # retranslateUi

