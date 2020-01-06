# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drrr_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Drrr(object):
    def setupUi(self, Drrr):
        Drrr.setObjectName("Drrr")
        Drrr.resize(650, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Drrr.sizePolicy().hasHeightForWidth())
        Drrr.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/drrr.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Drrr.setWindowIcon(icon)
        Drrr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Drrr)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(13, 13, 13, 13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QtWidgets.QWidget(Drrr)
        self.titleBar.setMinimumSize(QtCore.QSize(0, 30))
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleBar.setMouseTracking(True)
        self.titleBar.setStyleSheet(".QWidget\n"
"{\n"
"background:transparent;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background:black;\n"
"border:1px solid #000000;\n"
"}")
        self.titleBar.setObjectName("titleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_label = QtWidgets.QLabel(self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setMouseTracking(True)
        self.title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_label.setStyleSheet("background:black;\n"
"color:white;")
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setWordWrap(False)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.minBtn = QtWidgets.QPushButton(self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy)
        self.minBtn.setMinimumSize(QtCore.QSize(18, 18))
        self.minBtn.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.minBtn.setFont(font)
        self.minBtn.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"background-color:rgba(67,241,61,255);\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgba(76,252,68,255);\n"
"}")
        self.minBtn.setText("")
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout.addWidget(self.minBtn, 0, QtCore.Qt.AlignVCenter)
        self.maxBtn = QtWidgets.QPushButton(self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxBtn.sizePolicy().hasHeightForWidth())
        self.maxBtn.setSizePolicy(sizePolicy)
        self.maxBtn.setMinimumSize(QtCore.QSize(18, 18))
        self.maxBtn.setMaximumSize(QtCore.QSize(18, 18))
        self.maxBtn.setStyleSheet("QPushButton\n"
"{\n"
"background:transparent;\n"
"background-color:blue;\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgba(115,164,238,255);\n"
"}")
        self.maxBtn.setText("")
        self.maxBtn.setIconSize(QtCore.QSize(18, 18))
        self.maxBtn.setObjectName("maxBtn")
        self.horizontalLayout.addWidget(self.maxBtn, 0, QtCore.Qt.AlignVCenter)
        self.closeBtn = QtWidgets.QPushButton(self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QtCore.QSize(18, 18))
        self.closeBtn.setMaximumSize(QtCore.QSize(18, 18))
        self.closeBtn.setStyleSheet("QPushButton\n"
"{\n"
"background: transparent;\n"
"background-color:red;\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgba(255,140,140,255)\n"
"}")
        self.closeBtn.setText("")
        self.closeBtn.setIconSize(QtCore.QSize(18, 18))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addWidget(self.titleBar)
        self.centerStackedWidget = QtWidgets.QStackedWidget(Drrr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerStackedWidget.sizePolicy().hasHeightForWidth())
        self.centerStackedWidget.setSizePolicy(sizePolicy)
        self.centerStackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centerStackedWidget.setStyleSheet("")
        self.centerStackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.centerStackedWidget.setObjectName("centerStackedWidget")
        self.loginPage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginPage.sizePolicy().hasHeightForWidth())
        self.loginPage.setSizePolicy(sizePolicy)
        self.loginPage.setStyleSheet("QWidget\n"
"{\n"
"background-color:#000;\n"
"}")
        self.loginPage.setObjectName("loginPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loginPage)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 50)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QLabel(self.loginPage)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/img/drrr.png"))
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame = QtWidgets.QFrame(self.loginPage)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color:#000000;")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loginLabel = QtWidgets.QLabel(self.frame)
        self.loginLabel.setMinimumSize(QtCore.QSize(120, 30))
        self.loginLabel.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("color:#fff;")
        self.loginLabel.setObjectName("loginLabel")
        self.horizontalLayout_4.addWidget(self.loginLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.usernameEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameEdit.setMinimumSize(QtCore.QSize(180, 30))
        self.usernameEdit.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.usernameEdit.setFont(font)
        self.usernameEdit.setStyleSheet("background:transparent;\n"
"background-color:#fff;\n"
"border-radius:15px;\n"
"padding:0 10px")
        self.usernameEdit.setText("")
        self.usernameEdit.setObjectName("usernameEdit")
        self.horizontalLayout_4.addWidget(self.usernameEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        #=======================icones=============================#
        self.iconsBtn = QtWidgets.QPushButton(self.loginPage)
        self.iconsBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.iconsBtn.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iconsBtn.setFont(font)
        self.iconsBtn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(140, 140, 140);\n"
"border: 3px solid #fff;\n"
"border-radius: 8px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgb(189, 189, 189);\n"
"}")
        #========================enter_button============================#
        self.enterBtn = QtWidgets.QPushButton(self.loginPage)
        self.enterBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.enterBtn.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enterBtn.setFont(font)
        self.enterBtn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(140, 140, 140);\n"
"border: 3px solid #fff;\n"
"border-radius: 8px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgb(189, 189, 189);\n"
"}")
        self.enterBtn.setObjectName("enterBtn")
        self.iconsBtn.setObjectName("iconsBtn")
        self.verticalLayout_2.addWidget(self.enterBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.iconsBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.setStretch(0, 1)
        self.centerStackedWidget.addWidget(self.loginPage)
        #========================the end icone and enter botton============================#
        #=======================Final da tela de Login============================#
        self.room_search = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room_search.sizePolicy().hasHeightForWidth())
        self.room_search.setSizePolicy(sizePolicy)
        self.room_search.setStyleSheet("QWidget\n"
"{\n"
"background-color:#000000;\n"
"}")
        self.room_search.setObjectName("room_search")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.room_search)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.room_search)
        self.widget.setMinimumSize(QtCore.QSize(0, 170))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 170))
        self.widget.setStyleSheet(".QWidget\n"
"{\n"
"background:transparent;\n"
"}")


        # #-------------------------------------
        self.treeView = QtWidgets.QTreeView(self.room_search)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 660, 300))
        self.treeView.setObjectName("treeView")


        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'RoomId', 'language'])
        self.treeView.header().setDefaultSectionSize(180)
        self.treeView.setModel(self.model)
        self.treeView.setObjectName("TreeView")
        self.treeView.setStyleSheet("QFrame\n"
"{\n"
"background-color:black;\n"
"color:white;\n"
"border-radius:16px;\n"
"}")
        #self.verticalLayout_3.addWidget(self.treeView, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)



        # self.lineEdit = QtWidgets.QLineEdit(self.widget)
        # self.lineEdit.setGeometry(QtCore.QRect(560, 160, 171, 31))
        # self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setObjectName("teste_btn")
        # self.verticalLayout_3.addWidget(self.lineEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        # self.pushButton = QtWidgets.QPushButton(self.widget)
        # self.pushButton.setGeometry(QtCore.QRect(590, 200, 111, 41))
        # self.pushButton.setStyleSheet("background:blue;")
        # self.pushButton.setObjectName("pushButton")
        # self.pushButton.setObjectName("teste_btn")
        # self.verticalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)


## acabar de colocar as labeis 

        self.IDlabel = QtWidgets.QLabel(self.room_search)
        self.IDlabel.setGeometry(QtCore.QRect(145, 465, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.IDlabel.setFont(font)
        self.IDlabel.setStyleSheet("color:#fff;")
        self.IDlabel.setObjectName("IDlabel")


        self.lineEdit = QtWidgets.QLineEdit(self.room_search)
        self.lineEdit.setGeometry(QtCore.QRect(225, 460, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setObjectName("teste_btn")
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"background:white;\n"
"font-size: 20px;\n"
"border:none;\n"
"border-radius:15px;\n"
"color:black;\n"
"border-bottom:1px solid #717072;;\n"
"}")


        self.teste_btn = QtWidgets.QPushButton(self.room_search)
        self.teste_btn.setMinimumSize(QtCore.QSize(180, 30))
        self.teste_btn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.teste_btn.setGeometry(QtCore.QRect(220, 500, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.teste_btn.setFont(font)
        self.teste_btn.setStyleSheet(".QPushButton{\n"
"background-color:#333333;\n"
"border-radius:15px;\n"
"color:#ffffff;\n"
"border:1px solid #ccc;\n"
"}\n"
".QPushButton::hover{\n"
"background-color:#333333;\n"
"}")
        self.teste_btn.setObjectName("teste_btn")
        self.centerStackedWidget.addWidget(self.room_search)
        #========================the end room Searck============================#
        self.testPage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testPage.sizePolicy().hasHeightForWidth())
        self.testPage.setSizePolicy(sizePolicy)
        self.testPage.setStyleSheet("")
        self.testPage.setObjectName("testPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.testPage)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.testPage)
        self.widget.setMinimumSize(QtCore.QSize(0, 170))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 170))
        self.widget.setStyleSheet(".QWidget\n"
"{\n"
"background-color:#38383e;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color:#ffffff;")
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_2.addWidget(self.timeLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernameLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLabel.setStyleSheet("color:white;")
        self.horizontalLayout_2.addWidget(self.usernameLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.userBtn = QtWidgets.QToolButton(self.widget)
        self.userBtn.setMaximumSize(QtCore.QSize(17, 17))
        self.userBtn.setStyleSheet("background:transparent;")
        self.userBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/img/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userBtn.setIcon(icon1)
        self.userBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.userBtn.setAutoRaise(True)
        self.userBtn.setObjectName("userBtn")
        self.horizontalLayout_2.addWidget(self.userBtn)
        self.settingBtn = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingBtn.sizePolicy().hasHeightForWidth())
        self.settingBtn.setSizePolicy(sizePolicy)
        self.settingBtn.setMaximumSize(QtCore.QSize(17, 17))
        self.settingBtn.setStyleSheet("background:transparent;")
        self.settingBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/img/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingBtn.setIcon(icon2)
        self.settingBtn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.settingBtn.setAutoRaise(True)
        self.settingBtn.setObjectName("settingBtn")
        self.horizontalLayout_2.addWidget(self.settingBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("background-color:#38383e;")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(400, 70))
        self.textEdit.setMaximumSize(QtCore.QSize(400, 70))
        self.textEdit.setStyleSheet(".QTextEdit\n"
"{\n"
"background:transparent;\n"
"color:white;\n"
"background-color:#333333;\n"
"border-radius:15px;\n"
"border:1px solid #ccc;\n"
"padding:2px 5px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_5.addWidget(self.textEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setContentsMargins(5, -1, -1, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem3)
        self.limit = QtWidgets.QLabel(self.frame_2)
        self.limit.setMinimumSize(QtCore.QSize(80, 20))
        self.limit.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.limit.setFont(font)
        self.limit.setStyleSheet(".QLabel\n"
"{\n"
"color:#ffffff;\n"
"background:transparent\n"
"}")
        self.limit.setObjectName("limit")
        self.verticalLayout_5.addWidget(self.limit, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.postBtn = QtWidgets.QPushButton(self.widget)
        self.postBtn.setMinimumSize(QtCore.QSize(180, 30))
        self.postBtn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.postBtn.setFont(font)
        self.postBtn.setStyleSheet(".QPushButton{\n"
"background-color:#333333;\n"
"border-radius:15px;\n"
"color:#ffffff;\n"
"border:1px solid #ccc;\n"
"}\n"
".QPushButton::hover{\n"
"background-color:#333333;\n"
"}")
        self.postBtn.setObjectName("postBtn")
        self.verticalLayout_4.addWidget(self.postBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.widget)


        # self.textBrowser = QtWidgets.QTextBrowser(self.testPage)
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(12)
        # self.textBrowser.setFont(font)
        # self.textBrowser.setStyleSheet("background-color:#000000;\n"
        #                                "color:#ffffff;\n")
        # self.textBrowser.setDocumentTitle("")
        # self.textBrowser.setAcceptRichText(False)
        # self.textBrowser.setObjectName("textBrowser")
        # self.verticalLayout_3.addWidget(self.textBrowser)


        #chat
        self.project_title = QtWidgets.QLabel("Learn Python")
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.project_title.setFont(font)
        self.project_title.setStyleSheet("color:#000000;")
        self.project_title.setObjectName("project_title")

        self.project_title.setStyleSheet("background-color:#000000;\n"
                                        "color:#ffffff;\n")
        #self.grid_box = QtWidgets.QGridLayout()


        #self.list_widget =QListWidgetItem(self.testPage)
        #self.list_widget.setStyleSheet("background-color:#000000;\n"
        #                                "color:#ffffff;\n"


        self.map_l = QLabel()  # 头像显示
        self.map_l.setFixedSize(40, 25)
        self.maps = QPixmap(ship_photo).scaled(40, 25)
        self.map_l.setPixmap(maps)
        #--------------------#



        self.layout_main = QHBoxLayout(self.testPage)
        self.layout_main.addWidget(map_l)

        #--------------------#


        #self.koi = QListWidgetItem()
        #self.grid_box.addWidget(self.project_title, 1, 0)
        #self.setLayout(self.grid_box)




        self.verticalLayout_3.addWidget(self.list_widget)




        # self.IconLabel = QtWidgets.QLabel(self.textBrowser)
        # self.IconLabel.setStyleSheet("background:black;")
        # self.IconLabel.setObjectName("IconLabel")
        # self.verticalLayout_3.addWidget(self.IconLabel)




        self.centerStackedWidget.addWidget(self.testPage)
        self.verticalLayout.addWidget(self.centerStackedWidget)
        self.statusBar = QtWidgets.QWidget(Drrr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMinimumSize(QtCore.QSize(0, 30))
        self.statusBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.statusBar.setStyleSheet(".QWidget\n"
"{\n"
"background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:8px;\n"
"border-bottom-left-radius:8px;\n"
"background:black;\n"
"border:1px solid #000000;\n"
"}")
        self.statusBar.setObjectName("statusBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.statusBar)
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ipInfo = QtWidgets.QLabel(self.statusBar)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.ipInfo.setFont(font)
        self.ipInfo.setStyleSheet(".QLabel\n"
"{\n"
"color:white;\n"
"background:black\n"
"}")
        self.ipInfo.setObjectName("ipInfo")
        self.horizontalLayout_3.addWidget(self.ipInfo, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Info = QtWidgets.QLabel(self.statusBar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Info.setFont(font)
        self.Info.setStyleSheet(".QLabel\n"
"{\n"
"color:rgba(70, 70, 70, 255);\n"
"background:transparent\n"
"}")
        self.Info.setText("")
        self.Info.setObjectName("Info")
        self.horizontalLayout_3.addWidget(self.Info, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.statusBar)

        self.retranslateUi(Drrr)
        self.centerStackedWidget.setCurrentIndex(0)
        self.closeBtn.clicked.connect(Drrr.close)
        self.maxBtn.clicked.connect(Drrr.maxAndNormal)
        self.minBtn.clicked.connect(Drrr.showMinimized)
        self.usernameEdit.returnPressed.connect(self.enterBtn.click)
        QtCore.QMetaObject.connectSlotsByName(Drrr)
        Drrr.setTabOrder(self.usernameEdit, self.enterBtn)
        Drrr.setTabOrder(self.enterBtn, self.postBtn)
        Drrr.setTabOrder(self.iconsBtn, self.postBtn)
        Drrr.setTabOrder(self.postBtn, self.userBtn)
        Drrr.setTabOrder(self.userBtn, self.settingBtn)
        Drrr.setTabOrder(self.settingBtn, self.minBtn)
        Drrr.setTabOrder(self.minBtn, self.maxBtn)
        Drrr.setTabOrder(self.maxBtn, self.closeBtn)
        #Drrr.setTabOrder(self.closeBtn, self.grid_box)


    def retranslateUi(self, Drrr):
        _translate = QtCore.QCoreApplication.translate
        Drrr.setWindowTitle(_translate("Drrr", "Drrr"))
        self.title_label.setText(_translate("Drrr", "              DRRR"))
        self.loginLabel.setText(_translate("Drrr", "USERNAME:"))
        self.enterBtn.setText(_translate("Drrr", "ENTER"))
        self.iconsBtn.setText(_translate("Drrr", "ICON"))
        #---------------------rooms-------------------------------#
        self.teste_btn.setText(_translate("Drrr", "ENTER"))
        self.IDlabel.setText(_translate("Drrr", "ID ROOM:"))
        self.lineEdit.setText(_translate("Drrr", ""))
        #---------------------chat-------------------------------#
        self.timeLabel.setText(_translate("Drrr", "01/01 00:00"))
        self.usernameLabel.setText(_translate("Drrr", "USERNAME"))
        self.limit.setText(_translate("Drrr", "0/0"))
        self.postBtn.setText(_translate("Drrr", "POST"))
        self.ipInfo.setText(_translate("Drrr", ""))

import resource_rc
