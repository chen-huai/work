# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QMessage 例子
   1.关于对话框:about
   2.错误对话框:critical
   3.警告:warning
   4.提问:question
   5.消息:information

   有两点差异
   1.显示对话框图标不一样
   2.显示的按钮不一样
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WinForm( QWidget):  
	def __init__(self):  
		super(WinForm,self).__init__()  
		self.setWindowTitle("QMessageBox 例子")  
		self.resize(300, 100)              
		self.myButton = QPushButton(self)    
		self.myButton.setText("点击弹出消息框")  
		self.myButton.clicked.connect(self.msg)  

	def msg(self):  
        # 使用infomation信息框
		#self.sender().是调用的相应的控件
		reply = QMessageBox.information(self, "标题", "对话框消息正文", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )  
		print( reply )
		
if __name__ == '__main__':
	from PyQt5 import QtCore
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app= QApplication(sys.argv)    
	demo = WinForm()  
	demo.show() 
	sys.exit(app.exec_())
