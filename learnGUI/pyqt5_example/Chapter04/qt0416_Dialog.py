# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QDialog 例子对话框

1.QMessageBox,消息对话框
2.QColorDialog，颜色对话框
3.QFileDialog，显示文件打开或者保存
4.QFontDialog,显示或者设置字体
5.QInputDialog，用户输入对话框

   
  
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DialogDemo( QMainWindow ):

	def __init__(self, parent=None):
		super(DialogDemo, self).__init__(parent) 		
		self.setWindowTitle("Dialog 例子")
		self.resize(350,300)
    
		self.btn = QPushButton( self)
		self.btn.setText("弹出对话框")  
		self.btn.move(50,50)		
		self.btn.clicked.connect(self.showdialog)
                
	def showdialog(self ):
		dialog = QDialog()
		btn = QPushButton("ok", dialog )
		btn.move(50,50)
		dialog.setWindowTitle("Dialog")
		dialog.setWindowModality(Qt.ApplicationModal)#显示模式，主窗口不可用
		btn.clicked.connect(dialog.close)
		dialog.exec_()

if __name__ == '__main__':
	from PyQt5 import QtCore
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	demo = DialogDemo()
	demo.show()
	sys.exit(app.exec_())
