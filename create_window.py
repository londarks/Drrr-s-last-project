# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        createDialog.setObjectName("createDialog")
        createDialog.resize(400, 161)
        self.verticalLayout = QtWidgets.QVBoxLayout(createDialog)
        self.verticalLayout.setContentsMargins(13, 13, 13, 13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QtWidgets.QFrame(createDialog)
        self.titleBar.setMinimumSize(QtCore.QSize(0, 30))
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleBar.setStyleSheet("QFrame\n"
"{\n"
"background:transparent;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background:rgb(230, 230, 230);\n"
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
"background-color:orange;\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgba(248,198,148,255)\n"
"}")
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.titleBar)
        self.frame_2 = QtWidgets.QFrame(createDialog)
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"background-color:white;\n"
"border:1px solod #ccc;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:8px;\n"
"border-bottom-left-radius:8px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.portEdit = QtWidgets.QLineEdit(self.frame_3)
        self.portEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.portEdit.setMaximumSize(QtCore.QSize(60, 25))
        self.portEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.portEdit.setInputMask("")
        self.portEdit.setText("")
        self.portEdit.setObjectName("portEdit")
        self.horizontalLayout_2.addWidget(self.portEdit, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connectBtn = QtWidgets.QPushButton(self.frame_4)
        self.connectBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.connectBtn.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.connectBtn.setFont(font)
        self.connectBtn.setStyleSheet(".QPushButton{\n"
"background-color:#fcfcad;\n"
"border-radius:15px;\n"
"color:#464646;\n"
"border:1px solid #ccc;\n"
"}\n"
".QPushButton::hover{\n"
"background-color:#fcfccc;\n"
"}")
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_3.addWidget(self.connectBtn)
        self.cancelBtn = QtWidgets.QPushButton(self.frame_4)
        self.cancelBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.cancelBtn.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setStyleSheet(".QPushButton{\n"
"background-color:#fcfcad;\n"
"border-radius:15px;\n"
"color:#464646;\n"
"border:1px solid #ccc;\n"
"}\n"
".QPushButton::hover{\n"
"background-color:#fcfccc;\n"
"}")
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_3.addWidget(self.cancelBtn)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(createDialog)
        self.minBtn.clicked.connect(createDialog.showMinimized)
        self.closeBtn.clicked.connect(createDialog.close)
        self.cancelBtn.clicked.connect(createDialog.close)
        self.connectBtn.clicked.connect(createDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(createDialog)
        createDialog.setTabOrder(self.portEdit, self.connectBtn)
        createDialog.setTabOrder(self.connectBtn, self.cancelBtn)
        createDialog.setTabOrder(self.cancelBtn, self.minBtn)
        createDialog.setTabOrder(self.minBtn, self.closeBtn)

    def retranslateUi(self, createDialog):
        _translate = QtCore.QCoreApplication.translate
        createDialog.setWindowTitle(_translate("createDialog", "Muted"))
        self.label_2.setText(_translate("createDialog", "PORT:"))
        self.connectBtn.setText(_translate("createDialog", "Create"))
        self.cancelBtn.setText(_translate("createDialog", "Cancel"))

