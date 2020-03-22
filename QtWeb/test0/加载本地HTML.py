import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载本地例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # 加载外部的web界面
        file_path = os.path.join(os.getcwd(), 'index.html')
        file_path = file_path.replace('\\',  '/') # 这个不换显示不出来
        print(file_path)
        self.browser.load(QUrl(file_path))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
