#coding:utf-8

import os
import threading

import platform

class StartMonkeyService(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        #add 'chcp 437' to fix:unknown encoding 'ms936' 
        cmd = 'chcp 437 && monkeyrunner ' + os.getcwd()

        sysstr = platform.system()
        if (sysstr == "Windows"):
            cmd = cmd + '\\..\\services\\MonkeyGetBitmapService.py'
        elif (sysstr == "Linux" or sysstr == "Darwin"):
            cmd = cmd + '/../services/MonkeyGetBitmapService.py'
        else:
            print ("不支持的操作系统!!!!!")

        print cmd
        os.system(cmd)