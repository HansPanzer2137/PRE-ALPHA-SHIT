import socket
import time
import os

class Client():
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 2000

        self.ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ClientSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def connect(self):
        self.ClientSock.bind((self.ip, self.port))

    def connect2(self):
        self.ClientSock2.bind((self.ip, 2001))



app = Client()
app.connect()
app.connect2()



