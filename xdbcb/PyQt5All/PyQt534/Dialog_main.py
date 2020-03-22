# -*- coding: utf-8 -*-

"""
这是一个可以使用书写markdown语言的例子！
文章链接：http://www.xdbcb8.com/archives/670.html
"""

import sys
import markdown2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_main import Ui_MainWindow

class Dialog_main(QMainWindow, Ui_MainWindow):
    """
    markdown书写
    """
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(Dialog_main, self).__init__(parent)
        self.setupUi(self)

    def md2html(self, mdstr):
        '''
        markdown的转换
        '''
        extras = ['code-friendly', 'fenced-code-blocks', 'footnotes', 'tables', 'code-color', 'pyshell', 'nofollow', 'cuddled-lists', 'header ids', 'nofollow']
        
        html = """
        <html lang="zh-cn">
        <head>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <style>

 .hll { background-color: #ffffcc }
.c { color: #0099FF; font-style: italic } /* Comment */
.err { color: #AA0000; background-color: #FFAAAA } /* Error */
.k { color: #006699; font-weight: bold } /* Keyword */
.o { color: #555555 } /* Operator */
.ch { color: #0099FF; font-style: italic } /* Comment.Hashbang */
.cm { color: #0099FF; font-style: italic } /* Comment.Multiline */
.cp { color: #009999 } /* Comment.Preproc */
.cpf { color: #0099FF; font-style: italic } /* Comment.PreprocFile */
.c1 { color: #0099FF; font-style: italic } /* Comment.Single */
.cs { color: #0099FF; font-weight: bold; font-style: italic } /* Comment.Special */
.gd { background-color: #FFCCCC; border: 1px solid #CC0000 } /* Generic.Deleted */
.ge { font-style: italic } /* Generic.Emph */
.gr { color: #FF0000 } /* Generic.Error */
.gh { color: #003300; font-weight: bold } /* Generic.Heading */
.gi { background-color: #CCFFCC; border: 1px solid #00CC00 } /* Generic.Inserted */
.go { color: #AAAAAA } /* Generic.Output */
.gp { color: #000099; font-weight: bold } /* Generic.Prompt */
.gs { font-weight: bold } /* Generic.Strong */
.gu { color: #003300; font-weight: bold } /* Generic.Subheading */
.gt { color: #99CC66 } /* Generic.Traceback */
.kc { color: #006699; font-weight: bold } /* Keyword.Constant */
.kd { color: #006699; font-weight: bold } /* Keyword.Declaration */
.kn { color: #006699; font-weight: bold } /* Keyword.Namespace */
.kp { color: #006699 } /* Keyword.Pseudo */
.kr { color: #006699; font-weight: bold } /* Keyword.Reserved */
.kt { color: #007788; font-weight: bold } /* Keyword.Type */
.m { color: #FF6600 } /* Literal.Number */
.s { color: #CC3300 } /* Literal.String */
.na { color: #330099 } /* Name.Attribute */
.nb { color: #336666 } /* Name.Builtin */
.nc { color: #00AA88; font-weight: bold } /* Name.Class */
.no { color: #336600 } /* Name.Constant */
.nd { color: #9999FF } /* Name.Decorator */
.ni { color: #999999; font-weight: bold } /* Name.Entity */
.ne { color: #CC0000; font-weight: bold } /* Name.Exception */
.nf { color: #CC00FF } /* Name.Function */
.nl { color: #9999FF } /* Name.Label */
.nn { color: #00CCFF; font-weight: bold } /* Name.Namespace */
.nt { color: #330099; font-weight: bold } /* Name.Tag */
.nv { color: #003333 } /* Name.Variable */
.ow { color: #000000; font-weight: bold } /* Operator.Word */
.w { color: #bbbbbb } /* Text.Whitespace */
.mb { color: #FF6600 } /* Literal.Number.Bin */
.mf { color: #FF6600 } /* Literal.Number.Float */
.mh { color: #FF6600 } /* Literal.Number.Hex */
.mi { color: #FF6600 } /* Literal.Number.Integer */
.mo { color: #FF6600 } /* Literal.Number.Oct */
.sa { color: #CC3300 } /* Literal.String.Affix */
.sb { color: #CC3300 } /* Literal.String.Backtick */
.sc { color: #CC3300 } /* Literal.String.Char */
.dl { color: #CC3300 } /* Literal.String.Delimiter */
.sd { color: #CC3300; font-style: italic } /* Literal.String.Doc */
.s2 { color: #CC3300 } /* Literal.String.Double */
.se { color: #CC3300; font-weight: bold } /* Literal.String.Escape */
.sh { color: #CC3300 } /* Literal.String.Heredoc */
.si { color: #AA0000 } /* Literal.String.Interpol */
.sx { color: #CC3300 } /* Literal.String.Other */
.sr { color: #33AAAA } /* Literal.String.Regex */
.s1 { color: #CC3300 } /* Literal.String.Single */
.ss { color: #FFCC33 } /* Literal.String.Symbol */
.bp { color: #336666 } /* Name.Builtin.Pseudo */
.fm { color: #CC00FF } /* Name.Function.Magic */
.vc { color: #003333 } /* Name.Variable.Class */
.vg { color: #003333 } /* Name.Variable.Global */
.vi { color: #003333 } /* Name.Variable.Instance */
.vm { color: #003333 } /* Name.Variable.Magic */
.il { color: #FF6600 } /* Literal.Number.Integer.Long */
 table {
        font-family: verdana,arial,sans-serif;
        font-size:11px;
        color:#333333;
        border-width: 1px;
        border-color: #999999;
        border-collapse: collapse;
        }
th {
    background:#b5cfd2 url('cell-blue.jpg');
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #999999;
    }
td {
    background:#dcddc0 url('cell-grey.jpg');
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #999999;
    }
        </style>
        </head>
        <body>
            %s
        </body>
        </html>
        """
    # 具体的颜色样式我们使用CSS进行标记

        ret = markdown2.markdown(mdstr, extras=extras)
        # extras的说明：https://github.com/trentm/python-markdown2/wiki/Extras

        return html % ret 
    
    @pyqtSlot()
    def on_plainTextEdit_textChanged(self):
        """
        将markdown的内容转换成HTML语言
        """
        md = self.plainTextEdit.toPlainText()
        newhtml = self.md2html(md)
        self.textEdit.setHtml(newhtml)# 富文本显示出来

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dg = Dialog_main()
    dg.show()
    sys.exit(app.exec_())