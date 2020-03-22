# -*- coding: utf-8 -*-

"""
这是一个关于Web页面交互初探2（QWebChannel和QWebEngineView的综合使用）的小例子！
文章链接：http://www.xdbcb8.com/archives/1102.html
文章链接：http://www.xdbcb8.com/archives/1126.html
"""

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtProperty, pyqtSignal

"""
目前发现一个问题，js那边设置value值的时候每次都能触发Myshared中的Web2PyQt5Value（fset）
但是如果之后js读取value，就无法触发PyQt52WebValue（fget）
"""


class Myshared(QWidget):
    '''
    共享类
    '''

    finish = pyqtSignal(list)
    totalChanged = pyqtSignal(str)
    #自定义一个finish信号

    def __init__(self):
        super().__init__()
        self.info = '123 3333'

    def PyQt52WebValue(self):
        print('web getting', self.info)
        return self.info
    
    def Web2PyQt5Value(self, strs):
        '''
        获得Web页面传值后续处理
        '''
        self.info = strs.split()
        # 信息分成用户名和密码

        fullinfo = "用户名：{}，密码：{}".format(self.info[0], self.info[1])
        QMessageBox.information(self, "Web页面过来的值！", fullinfo)
        self.finish.emit(self.info)
        # 信号发出去

    value = pyqtProperty(str, fget=PyQt52WebValue, fset=Web2PyQt5Value)
    # value = pyqtProperty(str, fget=PyQt52WebValue, fset=Web2PyQt5Value, notify=totalChanged)

    # pyqtProperty()函数定义新的PyQt属性
    # fget是获取属性值的函数；fset是用于设置属性值的函数。
    # 这个知识点比较新，请到文章处仔细阅读！！