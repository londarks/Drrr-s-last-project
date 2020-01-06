# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_black_list(object):
    def setupUi(self, connectDialog):
        connectDialog.setObjectName("connectDialog")
        connectDialog.resize(400, 161)
        self.verticalLayout = QtWidgets.QVBoxLayout(connectDialog)
        self.verticalLayout.setContentsMargins(13, 13, 13, 13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QtWidgets.QFrame(connectDialog)
        self.titleBar.setMinimumSize(QtCore.QSize(0, 30))
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleBar.setStyleSheet("QFrame\n"
"{\n"
"background:black;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background:black;\n"
"border:1px solid #919191;\n"
"}")
        self.titleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleBar.setObjectName("titleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.minBtn = QtWidgets.QPushButton(self.titleBar)
        self.minBtn.setMinimumSize(QtCore.QSize(18, 18))
        self.minBtn.setMaximumSize(QtCore.QSize(18, 18))
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
        self.horizontalLayout.addWidget(self.minBtn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.closeBtn = QtWidgets.QPushButton(self.titleBar)
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
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.titleBar)

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


        self.retranslateUi(connectDialog)
        self.minBtn.clicked.connect(connectDialog.showMinimized)
        self.closeBtn.clicked.connect(connectDialog.close)

    def retranslateUi(self, connectDialog):
        _translate = QtCore.QCoreApplication.translate
        connectDialog.setWindowTitle(_translate("connectDialog", "connectDialog"))
