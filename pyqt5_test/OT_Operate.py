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
		self.pushButton_2.clicked.connect(self.otApplication)

		# self.nameItem(MyMainWindow)
		# QtCore.QMetaObject.connectSlotsByName(MyMainWindow)

	def getData(self):
		self.textBrowser.clear()
		global date
		global weekday
		global employeeName
		global sapNo
		global department
		global timeIn
		global timeOut
		global workHours
		global publicHoliday
		global address
		date = []
		weekday = []
		employeeName = []
		sapNo = []
		department = []
		timeIn = []
		timeOut = []
		workHours = []
		publicHoliday = []
		address = os.path.abspath('.')
		selectFile = QFileDialog.getOpenFileNames(self, '选择考勤数据文件','%s'%address,'files(*.xls*)')
		if selectFile[0] !=[]:
			n = 0
			for n in range(len(selectFile[0])):
				fileName = os.path.split(selectFile[0][n])[1]
				self.textBrowser.append('正在开始读取考勤数据,\n请完成后开始后续操作')
				self.textBrowser.append('%s:%s' % (n + 1, fileName))
				app.processEvents()
				excel = win32com.gencache.EnsureDispatch('Excel.Application')
				excel.Visible = 0
				excel.Application.DisplayAlerts = 0
				wb = excel.Workbooks.Open(r"%s" % selectFile[0][n].replace('/', '\\'))
				ws = wb.Worksheets('TA Report')


				# 老方法获取excel表格数据
				# column = 1
				# row = 10
				# oneRow = []
				# while ws.Cells(row, column).Value is not None:
				# 	oneRow.append(ws.Cells(row, column).Value)
				# 	column += 1
				# row = 11
				# while ws.Cells(row, 1).Value is not None:
				# 	date.append(ws.Cells(row, int(oneRow.index('Date'))+1).Value)
				# 	weekday.append(ws.Cells(row, int(oneRow.index('Weekday'))+1).Value)
				# 	employeeName.append(ws.Cells(row, int(oneRow.index('Employee Name'))+1).Value)
				# 	sapNo.append(ws.Cells(row, int(oneRow.index('SAP No'))+1).Value)
				# 	department.append(ws.Cells(row, int(oneRow.index('Department'))+1).Value)
				# 	timeIn.append(ws.Cells(row, int(oneRow.index('Time IN'))+1).Value)
				# 	timeOut.append(ws.Cells(row, int(oneRow.index('Time OUT'))+1).Value)
				# 	workHours.append(ws.Cells(row, int(oneRow.index('Work Hours'))+1).Value)
				# 	publicHoliday.append(ws.Cells(row, int(oneRow.index('Public Holiday'))+1).Value)
				# 	row += 1

				# 新方法获取表格数据
				# 获取Excel Data的范围,解决list(chain.from_iterable((('Chen Frank',),('Chen Nemo',))))解决二维元组变一位，并转化为列表
				row = ws.UsedRange.Rows.Count-1
				col = ws.UsedRange.Columns.Count
				oneRow = ws.Range(ws.Cells(10, 1), ws.Cells(10, col)).Value[0]
				date += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Date'))+1), ws.Cells(row, int(oneRow.index('Date'))+1)).Value))
				weekday += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Weekday'))+1), ws.Cells(row, int(oneRow.index('Weekday'))+1)).Value))
				employeeName += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Employee Name'))+1), ws.Cells(row, int(oneRow.index('Employee Name'))+1)).Value))
				sapNo += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('SAP No'))+1), ws.Cells(row, int(oneRow.index('SAP No'))+1)).Value))
				department += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Department'))+1), ws.Cells(row, int(oneRow.index('Department'))+1)).Value))
				timeIn += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Time IN'))+1), ws.Cells(row, int(oneRow.index('Time IN'))+1)).Value))
				timeOut += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Time OUT'))+1), ws.Cells(row, int(oneRow.index('Time OUT'))+1)).Value))
				workHours += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Work Hours'))+1), ws.Cells(row, int(oneRow.index('Work Hours'))+1)).Value))
				publicHoliday += list(chain.from_iterable(ws.Range(ws.Cells(11, int(oneRow.index('Public Holiday'))+1), ws.Cells(row, int(oneRow.index('Public Holiday'))+1)).Value))

				n += 1
			app.processEvents()
			excel.Quit()
			MyMainWindow.nameItem(self)
			self.textBrowser.append('已完成读取考勤数据')
			app.processEvents()
		else:
			self.textBrowser.append('请重新选择考勤数据')
	def nameItem(self):
		nameList =sorted(list(set(employeeName)))
		i = 1
		for each in nameList:
			self.comboBox_2.addItem(each)
			i += 1
			app.processEvents()

	def otApplication(self):
		# name = self.lineEdit.text()
		name = self.comboBox_2.currentText()
		if name == '':
			self.textBrowser.append('请输入名字')
			app.processEvents()
		else:
			content = self.comboBox.currentText()+' '+self.lineEdit.text()
			t = float(self.doubleSpinBox.text())
			t2 = float(self.doubleSpinBox_2.text())
			self.textBrowser.append('开始计算加班时间')
			self.textBrowser.append('%s' % (name))
			app.processEvents()
			excel = win32com.gencache.EnsureDispatch('Excel.Application')
			excel.Visible = 0
			excel.Application.DisplayAlerts = 0
			wb = excel.Workbooks.Open(r"%s\\Overtimes Application Form.xlsx" % address)
			# w=wb.sheetnames
			ws = wb.Worksheets('加班申请表-正式&派遣&外包')
			try:
				num = employeeName.index(name)
			except ValueError:
				self.textBrowser.append('请输入正确的名字')
				app.processEvents()
			else:
				ws.Cells(5, 3).Value = sapNo[num]
				ws.Cells(6, 3).Value = department[num]
				ws.Cells(5, 7).Value = name
				ws.Cells(6, 7).Value = calendar.month_abbr[int(time.strftime('%m'))]
				i = num
				n = 1
				row = 10
				while employeeName[i] == name :
					if (timeIn[i] is None) and (timeOut[i] is None):
						i += 1
						continue
					elif timeIn[i] is None:
						self.textBrowser.append('  %s-上班未打卡' % date[i])
						app.processEvents()
						i += 1
						continue
					elif timeOut[i] is None:
						self.textBrowser.append('  %s-上下班未打卡' % date[i])
						app.processEvents()
						i += 1
						continue
					else:
						# 工作日1，周末2，法定假日3
						# status = 1
						# 周末
						if (weekday[i] == 'Saturday') or (weekday[i] == 'Sunday'):
							if publicHoliday[i] is None:
								status = 2
							elif 'Weekend Workday' in publicHoliday[i]:
								status = 1
							elif 'Statutory Holiday' in publicHoliday[i]:
								status = 3
							else:
								status = 2
						# 工作日
						else:
							if publicHoliday[i] is None:
								status = 1
							elif 'Adjustment Holiday' in publicHoliday[i]:
								status = 2
							elif 'Statutory Holiday' in publicHoliday[i]:
								status = 3
							else:
								status = 1


						if status == 1:
							if workHours[i] <= t:
								i += 1
								continue
							else:
								ws.Cells(row, 1).Value = 'Weekday'
								ws.Cells(row, 2).Value = date[i]
								ws.Cells(row, 2).NumberFormat = "yyyy/mm/dd"
								ws.Cells(row, 3).Value = timeIn[i]
								ws.Cells(row, 4).Value = timeOut[i]
								ws.Cells(row, 5).Value = '=(D%s-C%s)*24-%s'%(row,row,t)
								ws.Cells(row, 5).NumberFormat = "0.0"
								ws.Cells(row, 7).Value = content
								row += 1
								i += 1
						elif status == 2:
							ws.Cells(row, 1).Value = 'Weekend'
							ws.Cells(row, 2).Value = date[i]
							ws.Cells(row, 2).NumberFormat = "yyyy/mm/dd"
							ws.Cells(row, 3).Value = timeIn[i]
							ws.Cells(row, 4).Value = timeOut[i]
							ws.Cells(row, 5).Value = '=(D%s-C%s)*24-%s' % (row, row,t2)
							ws.Cells(row, 5).NumberFormat = "0.0"
							ws.Cells(row, 7).Value = content
							row += 1
							i += 1
						else:
							ws.Cells(row, 1).Value = 'Statutory Holiday'
							ws.Cells(row, 2).Value = date[i]
							ws.Cells(row, 2).NumberFormat = "yyyy/mm/dd"
							ws.Cells(row, 3).Value = timeIn[i]
							ws.Cells(row, 4).Value = timeOut[i]
							ws.Cells(row, 5).Value = '=(D%s-C%s)*24-%s' % (row, row,t2)
							ws.Cells(row, 5).NumberFormat = "0.0"
							ws.Cells(row, 7).Value = content
							row += 1
							i += 1
				wb.SaveAs('%s\\%s Overtimes Application Form.xlsx' % (address, name))
				self.textBrowser.append('已完成加班计算')
				self.textBrowser.append('文件生产路径：%s' % address)
				app.processEvents()
				excel.Quit()
				reply = QMessageBox.information(self, '信息', '已完成加班计算，请点击下一位', QMessageBox.Yes ,
											 QMessageBox.Yes)


if __name__ == "__main__":
	import sys
	import os
	import time
	import datetime
	import calendar
	import win32com.client as win32com
	from win32com.client import Dispatch
	from itertools import chain
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	sys.exit(app.exec_())