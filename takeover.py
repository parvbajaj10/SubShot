from PyQt5 import QtCore, QtGui, QtWidgets
import os,webbrowser, time, subprocess
import re, platform, errno, core
from threading import Thread, Event

class Ui_takeoverWindow(object):
    def setupUi(self, takeoverWindow):
        takeoverWindow.setObjectName("takeoverWindow")
        takeoverWindow.setFixedSize(800, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.rootDir + "icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        takeoverWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(takeoverWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.takeoverBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.takeoverBox.setGeometry(QtCore.QRect(10, 10, 781, 461))
        self.takeoverBox.setObjectName("takeoverBox")
        self.takeoverprogressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.takeoverprogressBar.setGeometry(QtCore.QRect(10, 490, 781, 31))
        self.takeoverprogressBar.setProperty("value", 0)
        self.takeoverprogressBar.setObjectName("takeoverprogressBar")
        
        takeoverWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(takeoverWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        takeoverWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(takeoverWindow)
        self.statusbar.setObjectName("statusbar")
        takeoverWindow.setStatusBar(self.statusbar)

        self.retranslateUi(takeoverWindow)
        QtCore.QMetaObject.connectSlotsByName(takeoverWindow)    

    def retranslateUi(self, takeoverWindow):
        _translate = QtCore.QCoreApplication.translate
        takeoverWindow.setWindowTitle(_translate("takeoverWindow", "Takeover"))
        
    
    ############################ Global Variables ###########################
        
    slash = "\\" if platform.system()=="Windows" else "/"
    workingDir = os.path.dirname(os.path.realpath(__file__)) + slash
    rootDir = os.path.dirname(os.path.realpath(__file__)) + slash
    
    
    ######################## Behavior Functions ###########################
        
    def sleepTime(self, content):
        if len(content) > 10000:
            return 0.00001
        elif len(content) > 1000:
            return 0.001
        elif len(content) > 100:
            return 0.01
        else:
            return 0.1
    
    ######################## Validations ###########################
    
    def validatePath(self,path):
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
                
    
    ######################### Main Functionality ###########################

    def threadStart(self):
        self.takeoverprogressBar.setFormat('Please wait...')
        self.hostileThread = core.ProcessThread("ruby " + self.workingDir + self.slash +"hostiletakeover.rb")
        self.hostileThread.start()
        self.hostileThread.finished.connect(self.takeoverOutput)
        
    
    def takeoverOutput(self):
        self.takeoverprogressBar.setFormat('Running - %p%')
        inputPath = self.workingDir + "Output.txt"
        self.validatePath(inputPath)
        f = open(inputPath,"r")
        content = f.readlines()
        content = [x.strip() for x in content]

        takeoverprogressBarValue = 0
        takeoverprogressBarIncrementCount = 100/len(content)
        delay = self.sleepTime(content)
        
        for i in content:
            self.takeoverBox.append(i)
            takeoverprogressBarValue = takeoverprogressBarValue + takeoverprogressBarIncrementCount
            self.takeoverprogressBar.setProperty("value",takeoverprogressBarValue)
            time.sleep(delay)
        
        f.close()
        self.takeoverprogressBar.setFormat('Done!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    takeoverWindow = QtWidgets.QMainWindow()
    ui = Ui_takeoverWindow()
    ui.setupUi(takeoverWindow)
    takeoverWindow.show()
    sys.exit(app.exec_())
