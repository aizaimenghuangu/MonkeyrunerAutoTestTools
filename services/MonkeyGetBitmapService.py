#coding:utf-8

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import threading
import os
import time

class MonkeyGetBitmapService(threading.Thread):
    
    def __init__(self):
        #0表示结束线程，1表示循环运行线程
        self.ctrl = 0
        print 'start monkeyrunner'
        try:
            #print 'MonkeyRunner.waitForConnection()'
            self.device = MonkeyRunner.waitForConnection()
            
            try:
                name = self.device.getProperty('build.model')
                width = self.device.getProperty('display.width')
                height = self.device.getProperty('display.height')
            except Exception, e:
                raise e

            
            self.info = {"name":name,"width":width,"height":height}
            print self.info
            
            
            self.path = 'C:\\screenshot\\'
            self.filename = 'monkeyPic'
            if os.path.exists(self.path):
                print 'path is exit'
            else:
                print'creat the path'
                os.makedirs('C:\\screenshot\\')
                
#             file1 = open('C:\\screenshot\\info.txt','w')        
#             file1.write(self.info)
#             file1.close()

            file2 = open('C:\\screenshot\\infoCtrl.txt','w')
            file2.write('0')
            file2.close()

            file1 = open('C:\\screenshot\\info.txt','w')
            file1.write(name + '\n')
            file1.write(width + '\n')
            file1.write(height + '\n')
            file1.close()
            
            file2 = open('C:\\screenshot\\infoCtrl.txt','w')
            file2.write('1')
            file2.close()
            
        except Exception,e:
            print Exception,":",e


    def run(self):
        self.ctrl = 1
        while self.ctrl == 1:
            file = open('C:\\screenshot\\ctrl.txt','w')
            file.write('0')
#             print '0'
            file.close()
            result = self.device.takeSnapshot()
            result.writeToFile (self.path + self.filename + '.png', 'png')
            file = open('C:\\screenshot\\ctrl.txt','w')
            file.write('1')
            file.close()
#             print '1'
#             print 'thread is running'
            time.sleep(0.2)

    def closeThread(self):
        self.ctrl = 0

MonkeyGetBitmapService().run()