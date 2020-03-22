import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import QWebChannel
from shared import Myshared

"""
小结：
1  这个例子的作用就是，pyqt5通过JavaScript获取页面的数据
2  JavaScript的字典类型和python的可以直接互通
"""


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载本地例子')
        self.resize(330, 220)
        self.layout = QVBoxLayout()

        # 创建一个按钮去调用 JavaScript代码
        self.button = QPushButton('设置全名')
        self.button.clicked.connect(self.complete_name)

        self.btn_fix = QPushButton('修改共享值')
        self.btn_fix.clicked.connect(self.fix)

        # 接收web的值
        self.web_edit = QLineEdit()

        # 创建一个 QWebEngineView 对象
        self.browser = QWebEngineView()
        # 加载外部的web界面
        # file_path = os.path.join(os.getcwd(), 'webchannel.html').replace('\\', '/')  # 这个不换显示不出来
        file_path = QFileInfo("./webchannel.html").absoluteFilePath()
        # self.browser.load(QUrl(file_path))
        self.browser.load(QUrl("http://127.0.0.1:5500/web2pyqt5/webchannel.html"))

        # 把QWebView和button加载到layout布局中
        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.web_edit)
        self.layout.addWidget(self.btn_fix)
        self.setLayout(self.layout)

        self.channel = QWebChannel()
        self.shared = Myshared()
        self.set_channel()

    def set_channel(self):
        self.channel.registerObject("conn_shared", self.shared)
        self.browser.page().setWebChannel(self.channel)
        self.shared.finish[list].connect(self.set_line_edit)

    def set_line_edit(self, mylist):
        self.web_edit.setText(f'{mylist[0]}_{mylist[1]}')


    def __del__(self):
        '''
        删除相关对象
        '''
        self.browser.deleteLater()
        # 让系统加快释放这部分内存，避免QWebEngineView崩溃

    @staticmethod
    def js_callback(result):
        """
        用于接收返回值
        :param result:
        :return:
        """
        print(result, type(result))

    def complete_name(self):
        jscode = "PyQt52WebValue('{}','{}');".format('123', '#llll')
        self.browser.page().runJavaScript(jscode, self.js_callback)

    def fix(self):
        try:
            self.shared.value = 'uuuuuu kkkkk'
        except Exception as e:
            print(e)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
