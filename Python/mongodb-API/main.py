#simple API with pymongo and configparser
import sys
import os
import time
import platform
import os.path
import socket
import uuid
import re


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
            
    def GetOS(self):
        global python_clearTerminal        
        if(platform.system()=="Linux"):
            print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Your IP address: "+platform.system())
            self.os=platform.system()
            python_clearTerminal="clear"
        if(platform.system()=="Windows"):
            print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Your IP address: "+platform.system())
            self.os=platform.platform()
            python_clearTerminal="cls"
            
    def GetIP(self):
        try:
            self.ip=socket.gethostbyname(socket.gethostname())
            print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Your IP address: "+self.ip)
        except:
            print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Error: couldn't get your ip")

    def GetMAC(self):
        try:
            self.mac_addr=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Your MAC address: "+self.mac_addr)
        except:
             print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Error: couldn't get your MAC address")

            


            

            


    
def ConfigCreate():
    config=Config()
    if(config.configExist==False):
        config.GetOS()
        config.GetIP()
        config.GetMAC()

ConfigCreate()
log="API started"
print(time.strftime("%H:%M:%S", time.localtime())+"  "+log)
