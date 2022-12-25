#simple API with pymongo and configparser
import sys
import os
import time
import platform
import os.path
import socket
import uuid
import re
import urllib.request
import datetime

#import atexit

import pymongo #pip3 install pymongo
import configparser #pip3 install configparser
import base64

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
            print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Your OS address: "+platform.system())
            self.os=platform.system()
            python_clearTerminal="clear"
        if(platform.system()=="Windows"):
            print(time.strftime("%H:%M:%S", time.localtime())+"  "+"Your OS address: "+platform.system())
            self.os=platform.system()
            python_clearTerminal="cls"
            
    def GetIP(self):
        try:
            self.ip=urllib.request.urlopen('https://ident.me').read().decode('utf8')
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
        config['HOST-STATS']={}
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


class API_Database():
    def __init__(self):
        self.db="mongodb+srv://Hans:"+str(base64.b64decode('VG9waWsyMDE5').decode('ascii'))+"@cluster0.6uyzqoe.mongodb.net/"
        self.DATABASE="ERASMUS_SHIT"
        self.DBhost_stats="CLIENTS"
        self.DBinformations="Ersamus"


            

config=Config()        
def ConfigCreate():
    global config
    if(config.configExist==False):
        config.GetOS()
        config.GetIP()
        config.GetMAC()
        config.MakeConfig()
    if(config.configExist==True):
        config.GET_DATA()
        data_host.append(config.os)
        data_host.append(config.ip)
        data_host.append(config.mac_addr)
        print("Actual system stats")
        for i in range(len(data_host)):
            print(data_host[i])

def INSERT_HOST_DATA():
    global config
    API = API_Database()
    try:
        client=pymongo.MongoClient(API.db)
        mydb = client[API.DATABASE]
        print(mydb.list_collection_names())
        mycol = mydb[API.DBhost_stats]
        try:
            conHost={"name": str(config.os), "address": str(config.ip), "mac": str(config.mac_addr), "time": str((datetime.datetime.now()).strftime("%H:%M:%S")),"day": str((datetime.date.today()).strftime("%d/%m/%Y"))
            }

            inser_handler = mycol.insert_one(conHost)
            print(inser_handler.inserted_id)
        except:
            command = time.strftime("%H:%M:%S", time.localtime())+"  "+"Error: insert data not succesful"
            log_file.append(command+"\n")
            print(command)
    except:
        command = time.strftime("%H:%M:%S", time.localtime())+"  "+"Error: connection not established"
        log_file.append(command+"\n")
        print(command)

ConfigCreate()
INSERT_HOST_DATA()
log="API started"
print(time.strftime("%H:%M:%S", time.localtime())+"  "+log)
