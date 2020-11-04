import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import chicon  # 引用图标
from OT_UI import *

class MyMainWindow(QMainWindow, Ui_mainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.getData)
	def getData(self):
		self.textBrowser.clear()
		global date
		global weekday
		global employeeName
		global sapNo
		global department
		global timeIn
		global timeOut
		global publicHoliday
		date = []
		weekday = []
		employeeName = []
		sapNo = []
		department = []
		timeIn = []
		timeOut = []
		publicHoliday = []
		address = os.path.abspath('.')
		selectFile = QFileDialog.getOpenFileNames(self, '选择考勤数据文件','%s'%address,'files(*.xls*)')
		if selectFile[0] !=[]:
			n = 0
			for n in range(len(selectFile[0])):
				fileName = os.path.split(selectFile[0][n])[1]
				excel = win32com.gencache.EnsureDispatch('Excel.Application')
				excel.Visible = 0
				excel.Application.DisplayAlerts = 0
				self.textBrowser.append('正在开始读取考勤数据')
				self.textBrowser.append('%s:%s'%(n+1,fileName))
				wb = excel.Workbooks.Open(r"%s" % selectFile[0][n].replace('/', '\\'))
				ws = wb.Worksheets('TA Report')
				column = 1
				row = 10
				oneRow = []
				while ws.Cells(row, column).Value is not None:
					oneRow.append(ws.Cells(row, column).Value)
					column += 1
				row = 11
				while ws.Cells(row, 1).Value is not None:
					date.append(ws.Cells(row, column=int(oneRow.index('Date'))+1).Value)
					weekday.append(ws.Cells(row, column=int(oneRow.index('Weekday'))+1).Value)
					employeeName.append(ws.Cells(row, column=int(oneRow.index('Employee Name'))+1).Value)
					sapNo.append(ws.Cells(row, column=int(oneRow.index('SAP No'))+1).Value)
					department.append(ws.Cells(row, column=int(oneRow.index('Department'))+1).Value)
					timeIn.append(ws.Cells(row, column=int(oneRow.index('Time IN'))+1).Value)
					timeOut.append(ws.Cells(row, column=int(oneRow.index('Time OUT'))+1).Value)
					publicHoliday.append(ws.Cells(row, column=int(oneRow.index('Public Holiday'))+1).Value)
					row += 1
				n += 1
			excel.Quit()
		else:
			self.textBrowser.append('请重新选择考勤数据')
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
	sys.exit(app.exec_())