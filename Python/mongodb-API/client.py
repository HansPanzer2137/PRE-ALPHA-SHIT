import socket
import time
import sys
import os
import urllib.request
import uuid
import platform
import re

#downloaded via pip
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ControlPanelLogin(object):

    def ButtonClicked(self):
        print("clicked")

    def setupUi(self, ControlPanelLogin):
        ControlPanelLogin.setObjectName("ControlPanelLogin")
        ControlPanelLogin.setEnabled(True)
        ControlPanelLogin.resize(428, 245)
        ControlPanelLogin.setWindowTitle("LoginPanelLogin")
        ControlPanelLogin.setToolTip("")
        ControlPanelLogin.setWhatsThis("")
        ControlPanelLogin.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        ControlPanelLogin.setSizeGripEnabled(False)
        self.textEdit = QtWidgets.QTextEdit(ControlPanelLogin)
        self.textEdit.setGeometry(QtCore.QRect(160, 50, 231, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(ControlPanelLogin)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 100, 231, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(ControlPanelLogin)
        self.label.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ControlPanelLogin)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 71, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(ControlPanelLogin)
        self.pushButton.setGeometry(QtCore.QRect(280, 190, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ControlPanelLogin)
        QtCore.QMetaObject.connectSlotsByName(ControlPanelLogin)
        ControlPanelLogin.setTabOrder(self.textEdit, self.textEdit_2)
        ControlPanelLogin.setTabOrder(self.textEdit_2, self.pushButton)

    def retranslateUi(self, ControlPanelLogin):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ControlPanelLogin", "Login"))
        self.label_2.setText(_translate("ControlPanelLogin", "Password"))
        self.pushButton.setText(_translate("ControlPanelLogin", "LOGIN"))
        self.pushButton.clicked.connect(self.ButtonClicked)

class ConnectionVIASocket():
    def __init__(self):
        self.baobab = "127.0.0.1"
        self.mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        self.os = platform.system()
        self.sock2137 = 0
    def DebugSocket(self):
        if self.os == "Windows":
            os.system("cls")
        if self.os == "Linux":
            os.system("clear")
        print("-----------------------------------------------")
        print("Current ip address:      "+self.ip)
        print("Current MAC address:     "+self.mac)
        print("Current OS:              "+self.os)
    def TestConnectionToAPI_VIASocket(self):
        if self.os == "Windows":
            try:
                response = os.system("ping -n 1 " + self.baobab)
                if response == 0:
                    print("Connection via socket to API:        yes")
                else:
                    print("Error in response")
            except:
                print("Error in socket ping test")
        
        if self.os == "Linux":
            try:
                response = os.system("ping -c 1 " + self.baobab)
                if response == 0:
                    print("Connection via socket to API:        yes")
                else:
                    print("Error in response")
            except:
                print("Error in socket ping test")

    def GetCallBackPort(self):
        try:
            self.sock2137 = socket.socket()
            self.sock2137.connect((self.baobab, 2137))

            data = self.sock2137.recv(1024)
            print(data.decode())


        except:
            print("Error in Getting free connections")
            



app = QtWidgets.QApplication(sys.argv)
ControlPanelLogin = QtWidgets.QDialog()
ui = Ui_ControlPanelLogin()
ui.setupUi(ControlPanelLogin)
ControlPanelLogin.show()

sock = ConnectionVIASocket()
sock.DebugSocket()
sock.TestConnectionToAPI_VIASocket()
sock.GetCallBackPort()


sys.exit(app.exec())
