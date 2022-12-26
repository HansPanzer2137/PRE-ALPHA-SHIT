import socket
import time
import os

class Client():
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 2000

        self.ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)






