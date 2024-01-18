from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
import time
import os

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("SplashScreen.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
        os.startfile("path//to//main//file.py")
        time.sleep(10)
        quit()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
