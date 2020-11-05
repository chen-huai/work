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
				self.textBrowser.append('正在开始读取考勤数据')
				self.textBrowser.append('%s:%s' % (n + 1, fileName))
				app.processEvents()
				excel = win32com.gencache.EnsureDispatch('Excel.Application')
				excel.Visible = 0
				excel.Application.DisplayAlerts = 0
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
					date.append(ws.Cells(row, int(oneRow.index('Date'))+1).Value)
					weekday.append(ws.Cells(row, int(oneRow.index('Weekday'))+1).Value)
					employeeName.append(ws.Cells(row, int(oneRow.index('Employee Name'))+1).Value)
					sapNo.append(ws.Cells(row, int(oneRow.index('SAP No'))+1).Value)
					department.append(ws.Cells(row, int(oneRow.index('Department'))+1).Value)
					timeIn.append(ws.Cells(row, int(oneRow.index('Time IN'))+1).Value)
					timeOut.append(ws.Cells(row, int(oneRow.index('Time OUT'))+1).Value)
					workHours.append(ws.Cells(row, int(oneRow.index('Work Hours'))+1).Value)
					publicHoliday.append(ws.Cells(row, int(oneRow.index('Public Holiday'))+1).Value)
					row += 1
				n += 1
			self.textBrowser.append('已完成读取考勤数据')
			app.processEvents()
			excel.Quit()
		else:
			self.textBrowser.append('请重新选择考勤数据')
	def otApplication(self):
		name = self.lineEdit.text()
		if name == '':
			self.textBrowser.append('请输入名字')
			app.processEvents()
		else:
			content = self.comboBox.currentText()
			self.textBrowser.append('开始计算加班时间')
			self.textBrowser.append('%s' % (name))
			app.processEvents()
			excel = win32com.gencache.EnsureDispatch('Excel.Application')
			excel.Visible = 0
			excel.Application.DisplayAlerts = 0
			wb = excel.Workbooks.Open(r"%s\\Overtimes Application Form.xlsx" %address)
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
						self.textBrowser.append('%s' % date[i])
						self.textBrowser.append('上班未打卡')
						app.processEvents()
						i += 1
						continue
					elif timeOut[i] is None:
						self.textBrowser.append('%s' % date[i])
						self.textBrowser.append('下班未打卡')
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
							if workHours[i] <= 9:
								i += 1
								continue
							else:
								ws.Cells(row, 1).Value = 'Weekday'
								ws.Cells(row, 2).Value = date[i]
								ws.Cells(row, 3).Value = timeIn[i]
								ws.Cells(row, 4).Value = timeOut[i]
								ws.Cells(row, 5).Value = '=(D%s-C%s)*24-9'%(row,row)
								ws.Cells(row, 5).NumberFormat = "0.0"
								row += 1
								i += 1
						elif status == 2:
							ws.Cells(row, 1).Value = 'Weekend'
							ws.Cells(row, 2).Value = date[i]
							ws.Cells(row, 3).Value = timeIn[i]
							ws.Cells(row, 4).Value = timeOut[i]
							ws.Cells(row, 5).Value = '=(D%s-C%s)*24-1' % (row, row)
							ws.Cells(row, 5).NumberFormat = "0.0"
							row += 1
							i += 1
						else:
							ws.Cells(row, 1).Value = 'Statutory Holiday'
							ws.Cells(row, 2).Value = date[i]
							ws.Cells(row, 3).Value = timeIn[i]
							ws.Cells(row, 4).Value = timeOut[i]
							ws.Cells(row, 5).Value = '=(D%s-C%s)*24-1' % (row, row)
							ws.Cells(row, 5).NumberFormat = "0.0"
							row += 1
							i += 1
				# i = 0
				# n = 1
				# row = 10
				# for i in range(len(employeeName)):
				# 	if employeeName[i] != name:
				# 		continue
				# 	else:
				# 		if (timeIn[i] is None) and (timeOut[i] is None):
				# 			continue
				# 		elif timeIn[i] is None:
				# 			self.textBrowser.append('%s' % date[i])
				# 			self.textBrowser.append('上班未打卡')
				# 			app.processEvents()
				# 			continue
				# 		elif timeOut[i] is None:
				# 			self.textBrowser.append('%s' % date[i])
				# 			self.textBrowser.append('下班未打卡')
				# 			app.processEvents()
				# 			continue
				# 		else:
				# 			# print(timeIn[i])
				# 			# a = datetime.datetime.strptime(str(timeIn[i]), "%H:%M")
				# 			# b = datetime.datetime.strptime(str(timeOut[i]), "%H:%M")
				# 			# c = int((b - a).seconds) / 3600
				# 			# if c % 0.5 > 0.41:
				# 			# 	d = c // 0.5 * 0.5 + 0.5
				# 			# else:
				# 			# 	d = c // 0.5 * 0.5
				#
				# 			# 工作日1，周末2，法定假日3
				# 			status = 1
				# 			# 周末
				# 			if (weekday[i] != 'Saturday') or (weekday[i] != 'Sunday'):
				# 				if publicHoliday[i] is None:
				# 					status = 1
				# 				elif 'Adjustment Holiday' in publicHoliday[i]:
				# 					status = 2
				# 				elif 'Statutory Holiday' in publicHoliday[i]:
				# 					status = 3
				#
				# 			# 工作日
				# 			else:
				# 				if publicHoliday[i] is None:
				# 					status = 2
				# 				if 'Weekend Workday' in publicHoliday[i]:
				# 					status = 1
				# 				elif 'Statutory Holiday' in publicHoliday[i]:
				# 					status = 3
				#
				# 			if status == 1:
				# 				if workHours[i] <= 9:
				# 					continue
				# 				else:
				# 					ws.Cells(row, 1).Value = 'Weekday'
				# 					ws.Cells(row, 2).Value = date[i]
				# 					ws.Cells(row, 3).Value = timeIn[i]
				# 					ws.Cells(row, 4).Value = timeOut[i]
				# 					ws.Cells(row, 5).Value = '=(D%s-C%s)*24-9'%(row,row)
				# 					ws.Cells(row, 5).NumberFormat = "0.0"
				# 					row += 1
				# 			elif status == 2:
				# 				ws.Cells(row, 1).Value = 'Weekend'
				# 				ws.Cells(row, 2).Value = date[i]
				# 				ws.Cells(row, 3).Value = timeIn[i]
				# 				ws.Cells(row, 4).Value = timeOut[i]
				# 				ws.Cells(row, 5).Value = '=(D%s-C%s)*24-1' % (row, row)
				# 				ws.Cells(row, 5).NumberFormat = "0.0"
				# 				row += 1
				# 			else:
				# 				ws.Cells(row, 1).Value = 'Statutory Holiday'
				# 				ws.Cells(row, 2).Value = date[i]
				# 				ws.Cells(row, 3).Value = timeIn[i]
				# 				ws.Cells(row, 4).Value = timeOut[i]
				# 				ws.Cells(row, 5).Value = '=(D%s-C%s)*24-1' % (row, row)
				# 				ws.Cells(row, 5).NumberFormat = "0.0"
				# 				row += 1
				wb.SaveAs('%s\\%s Overtimes Application Form.xlsx' % (address, name))
				self.textBrowser.append('已完成加班计算')
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
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	sys.exit(app.exec_())