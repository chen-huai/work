import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import chicon  # 引用图标
from OT_UI import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.getData)
	def getData(self):
		self.textBrowser.clear()
		selectBatchFile = QFileDialog.getOpenFileNames(self, '选择考勤数据文件','.','files(*.xls*)')
		excel = win32com.gencache.EnsureDispatch('Excel.Application')
		excel.Visible = 0
		excel.Application.DisplayAlerts = 0
		wb = excel.Workbooks.Open(r"%s" % selectBatchFile[0][0].replace('/', '\\'))
		ws = wb.Worksheets('TA Report')
		column = 1
		row = 10
		oneRow = []
		while ws.Cells(row, column).Value is not None:
			oneRow.append(ws.Cells(row, column).Value)
			column += 1

if __name__ == "__main__":
	import sys
	import os
	import time
	import random
	import pyautogui
	import pandas as pd
	import re
	import win32com.client as win32com
	from win32com.client import Dispatch
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	# myWin.getConfig()
	sys.exit(app.exec_())