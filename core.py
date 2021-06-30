from PyQt5 import QtCore
from threading import Thread, Event
import subprocess
from subprocess import PIPE

class ProcessThread(QtCore.QThread):
    def __init__(self, command):
        super(ProcessThread, self).__init__()
        self.command = command

    def run(self):
        subprocess.run(self.command, shell=True, stdout=subprocess.DEVNULL)

    def stop(self):
        self._isRunning = False
        self.terminate()
        self.wait(100)