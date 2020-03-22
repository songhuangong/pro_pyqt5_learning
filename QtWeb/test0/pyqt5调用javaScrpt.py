import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

"""
小结：
1  这个例子的作用就是，pyqt5通过JavaScript获取页面的数据
2  JavaScript的字典类型和python的可以直接互通
"""

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载本地例子')
        self.resize(330, 150)
        self.layout = QVBoxLayout()

        # 创建一个按钮去调用 JavaScript代码
        self.button = QPushButton('设置全名')
        self.button.clicked.connect(self.complete_name)

        # 创建一个 QWebEngineView 对象
        self.browser = QWebEngineView()
        # 加载外部的web界面
        file_path = os.path.join(os.getcwd(), 'index2.html').replace('\\', '/')  # 这个不换显示不出来
        self.browser.load(QUrl(file_path))
        # 把QWebView和button加载到layout布局中
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    @staticmethod
    def js_callback(result):
        print(result, type(result))

    def js_callback2(self, result):
        print(result, type(result))

    def complete_name(self):
        self.browser.page().runJavaScript('javascript_func();', self.js_callback2)
        # jscode = "PyQt52WebValue('{}','{}');".format(name, pwd)
        # self.view.page().runJavaScript(jscode)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
