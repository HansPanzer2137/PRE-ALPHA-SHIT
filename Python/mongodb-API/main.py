#simple API with pymongo and configparser
import sys
import os
import time
import platform
import os.path
import socket
import uuid
import re
#import atexit

import pymongo #pip3 install pymongo
import configparser #pip3 install configparser


log_file=[]
data_host=[]

class Config():
    def __init__(self) -> None:
        global log_file
        self.configExist=False 
        self.os=0
        self.ip=0
        self.mac_addr=0

        if(os.path.exists("config.majster")==True):
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
            command=time.strftime("%H:%M:%S", time.localtime())+"  "+"Your MAC address: "+self.mac_addr
            log_file.append(command+"\n")
            print(command)
        except:
            command=time.strftime("%H:%M:%S", time.localtime())+"  "+"Error: couldn't get your MAC address"
            log_file.append(command+"\n")
            print(command)

    def MakeConfig(self):
        config = configparser.ConfigParser()
        config['HOST-STATS']['OS']=self.os
        config['HOST-STATS']['IP']=self.ip
        config['HOST-STATS']['MAC']=self.mac_addr
        with open('config.majster', 'w') as configfile:
            config.write(configfile)

    def GET_DATA(self):
        config = configparser.ConfigParser()
        config.read('config.majster')
        self.os=config['HOST-STATS']['OS']
        self.ip=config['HOST-STATS']['IP']
        self.mac_addr=config['HOST-STATS']['MAC']




            

            


    
def ConfigCreate():
    config=Config()
    if(config.configExist==False):
        config.GetOS()
        config.GetIP()
        config.GetMAC()
    if(config.configExist==True):
        config.GET_DATA()
        data_host.append(config.os)
        data_host.append(config.ip)
        data_host.append(config.mac_addr)
            

ConfigCreate()
log="API started"
print(time.strftime("%H:%M:%S", time.localtime())+"  "+log)
