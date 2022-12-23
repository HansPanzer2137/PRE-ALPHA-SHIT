#simple API with pymongo and configparser
import sys
import os
import time
import platform
import os.path
import socket


import pymongo #pip3 install pymongo
import configparser #pip3 install configparser



class Config():
    def __init__(self) -> None:
        self.configExist=False 
        self.os=0
        self.ip=0
        self.mac_addr=0

        if(os.path.exists("Config.majster")==True):
            self.configExist=True
        else:
            if(platform.platform()=="Linux"):
                self.os=platform.platform()
            if(platform.platform()=="Windows"):
                self.os=platform.platform()
            try:
                socket.gethostbyname(socket.gethostname())
            except:
                print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Error: couldn't get your ip")

            


    


log="API started"
print(time.strftime("%H:%M:%S", time.localtime())+"  "+log)
