# -*- coding: utf-8 -*-
# Created by DoSun on 2017/5/20
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.uic import *
from drrr_window import *
import network
import cookie
import os
import threading

__version__ = '1.0'
MAX_LENGTH = 140
# SIZEOF_UINT16 = 2

UiFile = 'drrr_window.ui'


# Ui_Drrr, QtBaseClass = loadUiType(UiFile)


class ShadowWindow(QWidget):
    """构造有底部阴影的窗口类"""

    def __init__(self):
        super(ShadowWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.SHADOW_WIDTH = 15

    def drawShadow(self, painter):
        painter.drawPixmap(0,
                           0,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/left_top.png'))
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH,
                           0,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/right_top.png'))
        painter.drawPixmap(0,
                           self.height() - self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/left_bottom.png'))
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH,
                           self.height() - self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/right_bottom.png'))
        painter.drawPixmap(0,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/left_mid.png').scaled(self.SHADOW_WIDTH,
                                                                       self.height() - 2 * self.SHADOW_WIDTH))
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/right_mid.png').scaled(self.SHADOW_WIDTH,
                                                                        self.height() - 2 * self.SHADOW_WIDTH))
        painter.drawPixmap(self.SHADOW_WIDTH,
                           0,
                           self.width() - 2 * self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/top_mid.png').scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                                      self.SHADOW_WIDTH))
        painter.drawPixmap(self.SHADOW_WIDTH,
                           self.height() - self.SHADOW_WIDTH,
                           self.width() - 2 * self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/bottom_mid.png').scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                                         self.SHADOW_WIDTH))

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)


# class black_list(QDialog, ShadowWindow, Ui_connectDialog):
#     """连接服务器对话框"""

#     def __init__(self):
#         super(black_list, self).__init__()
#         self.setupUi(self)


class Backend(QThread):
    """atualiza data/hora"""
    updateDate = pyqtSignal(str)

    def run(self):
        while True:
            dateNow = QDate.currentDate().toString('MM/dd')
            timeNow = QTime.currentTime().toString('hh:mm')
            dateTime = dateNow + ' ' + timeNow
            self.updateDate.emit(dateTime)
            time.sleep(1)


class DrrrMainWindow(Ui_Drrr, ShadowWindow):
    """主窗口"""
    updateClients = pyqtSignal(str)

    def __init__(self):
        """主窗口的各项参数初始化"""
        super(DrrrMainWindow, self).__init__()
        self.setupUi(self)
        self.__leftButtonPress = False
        self.__movePoint = QPoint()
        self.tooMany = False

        self.today = QDate()

        self.textEdit.installEventFilter(self)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.document().setMaximumBlockCount(2)
        self.textEdit.textChanged.connect(self.maxLength)

        # html_pattern = '''
        # <html><head></head>
        # <body style='color:green'>
        # </body>
        # </html>
        # '''
        # self.textBrowser.setHtml(html_pattern)

        self.Binding()
        # t_info = threading.Thread(target=self.msg_loop)
        # t_info.start()

    def maxLength(self):
        """判断输入文本字数长度是否超过限制"""
        text = self.textEdit.toPlainText()
        length = len(text)
        self.limit.setText(str(length) + r'/' + str(MAX_LENGTH))
        if length > MAX_LENGTH:
            self.tooMany = True
        else:
            self.tooMany = False

    def msg_loop(self,):
        enter_room = network.Commands()
        url_room = 'https://drrr.com/room/?id=Isv7xLNDcP'
        file_name = 'athus.cookie'
        name = ''+self.usernameLabel.text()
        print(name)
        icon = 'zaika'
        save = cookie.Cookie_Server(name=name, icon=icon)
        if not os.path.isfile(file_name):
            save.login()
            save.save_cookie(file_name=file_name)
        while 1:
            enter_room.load_cookie(file_name=file_name)
            e_room = enter_room.room_enter(url_room=url_room)
            message = enter_room.room_update(room_text=e_room)
            name_sender = enter_room.room_update(room_text=e_room)
            #self.loop_msg(username=name_sender[1],msg=message[0])
            self.listWidget.insertItem( 0, "@{}:{}".format(name_sender[1],message[0]))
        # menssage = 'Londarks'
        # rooms = self.session.get("https://drrr.com/lounge?api=json")
        # salas = []
        # if rooms.status_code == 200:
        #     rooms_data = json.loads(rooms.content)
        # for rooms in rooms_data['rooms']:
        #     salas.append(rooms)
        # # Adicionando parametros a salas
        # for j in range(len(salas)):
        #   # it = QtGui.QStandardItem(salas[j]['name'])
        #   self.model.appendRow([QtGui.QStandardItem(salas[j]['name']),
        #                        QtGui.QStandardItem(salas[j]['roomId']),
        #                        QtGui.QStandardItem(salas[j]['language']),
        #                        ])
        # self.itemOld = QtGui.QStandardItem("text")

    def send_message(self, msg):
        enter_room = network.Commands()
        #send = enter_room.send_message(msg=msg)
        file_name = 'athus.cookie'
        enter_room.load_cookie(file_name=file_name)
        target = enter_room.post(message=msg)

    def Binding(self):
        """inicializador"""
        #self.MenuBinding()
        self.enterBtn.clicked.connect(self.updateBrowser)
        self.postBtn.clicked.connect(self.postMsg)

    def MenuBinding(self):
        """menu-chat"""
        settingMenu = QMenu(self)
        whitelist = QAction('whitelist', self)
        blacklist = QAction('blacklist', self)
        twitter = QAction('twitter', self)
        feedback = QAction('feedback', self)
        settingMenu.addActions([whitelist, blacklist, twitter, feedback])
        self.settingBtn.setMenu(settingMenu)
        #connectBtn.triggered.connect(self.connectServer)
        #createBtn.triggered.connect(self.black_list)



    def updateBrowser(self, msg):
        t_info = threading.Thread(target=self.postName)
        t_info.start()
        t_info = threading.Thread(target=self.msg_loop)
        t_info.start()

    def postName(self):
        """muda de freme/impede de serguir com nome vazio"""
        self.Info.clear()
        if not self.usernameEdit.text():
            self.Info.setText('Write a username')
        else:
            self.usernameLabel.setText(self.usernameEdit.text())
            self.centerStackedWidget.setCurrentIndex(2)
            self.textEdit.setFocus()

    def setDate(self, dateTime):
        """Mostra a hora"""
        self.timeLabel.setText(dateTime)

    def postMsg(self):
        """painel de enviar menssagem"""
        self.Info.clear()
        if not self.textEdit.toPlainText():
            self.Info.setText('Write a message.!!!.')
            return
        if '/leave' == self.usernameEdit.text():
            self.centerStackedWidget.setCurrentIndex(1)
        if self.tooMany:
            self.Info.setText('Exceeded character limit' + str(MAX_LENGTH))
            return
        #msg = self.usernameLabel.text() + ': ' + self.textEdit.toPlainText()
        msg = '' + self.textEdit.toPlainText()
        self.textEdit.clear()
        # envia menssagem
        self.send_message(msg)

    #   event mouse
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.titleBar.rect().contains(event.pos()):
                self.__leftButtonPress = True
                self.__movePoint = event.pos()

    def mouseMoveEvent(self, event):
        if self.__leftButtonPress:
            globalPos = event.globalPos()
            self.move(globalPos - self.__movePoint)

    def mouseReleaseEvent(self, event):
        self.__leftButtonPress = False

    def maxAndNormal(self):
        """maximo/minimo windows"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    drrr = DrrrMainWindow()
    backend = Backend()
    backend.updateDate.connect(drrr.setDate)
    backend.start()
    drrr.show()
    app.exec_()
