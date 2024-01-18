from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

UIPath = r"C:\Users\yash3\OneDrive\Desktop\Yash12007\Projects\WEBVIEW\SplashScreen\SplashScreen.ui"

class SplashScreen(QMainWindow):
    def __init__(self):
        
        super(SplashScreen, self).__init__()
        uic.loadUi(UIPath, self)
        self.progress = self.findChild(QProgressBar, 'progressBar')
        self.quit = self.findChild(QPushButton, 'Quit')
        self.status = self.findChild(QLabel, 'status')
        self.quit.clicked.connect(self.close)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.loading_steps = ["Initializing...", "Loading...", "Almost there...", "Finishing up..."]
        self.current_step = 0
        self.loading_timer = QTimer(self)
        self.loading_timer.timeout.connect(self.update_loading)
        self.loading_timer.start(1000)
        self.show()

    def close(self):
        super(SplashScreen, self).close()

    def update_loading(self):
        if self.current_step < len(self.loading_steps) - 1:
            self.progress.setValue(self.progress.value() + 25)
            self.status.setText(self.loading_steps[self.current_step])
            self.current_step += 1
        else:
            self.loading_timer.disconnect()
            uic.loadUi("C:\\Users\\yash3\\OneDrive\\Desktop\\Yash12007\\Projects\\WEBVIEW\\Nexus_OS\\1280x720.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = SplashScreen()
    sys.exit(app.exec_())
