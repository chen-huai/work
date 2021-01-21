import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import chicon  # 引用图标
from Reach_Operate_Ui import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)

		self.actionExport.triggered.connect(self.exportConfig)
		self.actionImport.triggered.connect(self.importConfig)
		self.actionExit.triggered.connect(MyMainWindow.close)
		self.pushButton_3.clicked.connect(self.searchReachMessage)
		self.actionImport.triggered.connect(self.lineEdit.clear)
		self.actionHelp.triggered.connect(self.lineEdit.clear)
		self.actionAuthor.triggered.connect(self.showAuthorMessage)
		self.pushButton_2.clicked.connect(self.getReachMessage)
		self.pushButton_1.clicked.connect(self.textBrowser.clear)
		self.pushButton_1.clicked.connect(self.lineEdit.clear)
		self.pushButton_1.clicked.connect(self.lineEdit_1.clear)


	def getConfig(self):
		# 初始化，获取或生成配置文件
		global configFileUrl
		global desktopUrl
		global now
		global last_time
		global today
		# getReachMessage
		global reachLimsNo
		global reachEnglish
		global reachChinese
		global reachCas
		global reachPurpose
		now = int(time.strftime('%Y'))
		last_time = now - 1
		today = time.strftime('%Y%m%d')
		desktopUrl = os.path.join(os.path.expanduser("~"), 'Desktop')
		configFileUrl = '%s/config' % desktopUrl
		configFile = os.path.exists('%s/config_reach.txt' % configFileUrl)
		# print(desktopUrl,configFileUrl,configFile)
		if not configFile:  # 判断是否存在文件夹如果不存在则创建为文件夹
			reply = QMessageBox.question(self, '信息', '确认是否要创建配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if reply == QMessageBox.Yes:
				if not os.path.exists(configFileUrl):
					os.makedirs(configFileUrl)
				MyMainWindow.createConfigContent(self)
				MyMainWindow.getConfigContent(self)
				self.textBrowser.setText("创建并导入配置成功")
			else:
				exit()
		else:
			MyMainWindow.getConfigContent(self)

	def getConfigContent(self):
		# 获取配置文件内容
		f1 = open('%s/config_reach.txt' % configFileUrl, "r", encoding="utf-8")
		global configContent
		configContent = {}
		i = 0
		for line in f1:
			if line != '\n':
				lineContent = line.split('||||||')
				# print(lineContent)
				configContent['%s' % lineContent[0]] = lineContent[1].split('\n')[0]
			i += 1
		# print(configContent)
		self.textBrowser.setText("配置获取成功")

	def createConfigContent(self):
		# 生成默认配置文件
		configContentName = ['选择ICP_Batch的输入路径和结果输出路径', 'Reach_Message_File_Name']
		configContent = ['默认，可更改为自己需要的', 'REACH_SVHC_Candidate_List.csv']
		f1 = open('%s/config_reach.txt' % configFileUrl, "w", encoding="utf-8")
		i = 0
		for i in range(len(configContentName)):
			f1.write(configContentName[i] + '||||||' + configContent[i] + '\n')
			i += 1
		self.textBrowser.setText("配置文件创建成功")
		QMessageBox.information(self, "提示信息",
								"默认配置文件已经创建好，\n如需修改请在用户桌面查找config文件夹中config_reach.txt，\n将相应的文件内容替换成用户需求即可，修改后记得重新导入配置文件。\n切记：中间‘||||||’六根，不能多也不能少！！！",
								QMessageBox.Yes)

	def exportConfig(self):
		# 重新导出默认配置文件
		reply = QMessageBox.question(self, '信息', '确认是否要创建默认配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if reply == QMessageBox.Yes:
			MyMainWindow.createConfigContent(self)
		else:
			QMessageBox.information(self, "提示信息", "没有创建默认配置文件，保留原有的配置文件", QMessageBox.Yes)

	def importConfig(self):
		# 重新导入配置文件
		reply = QMessageBox.question(self, '信息', '确认是否要导入配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if reply == QMessageBox.Yes:
			MyMainWindow.getConfigContent(self)
		else:
			QMessageBox.information(self, "提示信息", "没有重新导入配置文件，将按照原有的配置文件操作", QMessageBox.Yes)

	def showAuthorMessage(self):
		# 关于作者
		QMessageBox.about(self, "关于",
						  "人生苦短，码上行乐。\n\n\n        ----Frank Chen")


	def getReachMessage(self):
		# 获取Reach信息
		global reachLimsNo
		global reachEnglish
		global reachChinese
		global reachCas
		global reachPurpose
		file = configContent['Reach_Message_Import_URL'] + '\\' + configContent['Reach_Message_File_Name']
		folder = os.path.exists(file)
		if not folder:
			QMessageBox.information(self, "无Reach信息模板",
									"没有Reach信息文件！！！\n请查看config配置文件内容是否符合需求。\nReach_Message_Import_URL,Reach_Message_File_Name\nReach Message的文件路径、文件名称和CSV格式",
									QMessageBox.Yes)
		else:
			reachMessage = pd.read_csv(file)
			reachLimsNo = list(reachMessage['Lims No.'])
			reachEnglish = list(reachMessage['物质名称(英文)'])
			reachChinese = list(reachMessage['物质名称(中文)'])
			reachCas = list(reachMessage['CAS 号码'])
			reachPurpose = list(reachMessage['可能用途'])
			self.textBrowser.setText("Reach信息获取成功")

	def searchReachMessage(self):
		# 搜索Reach信息提示
		try:
			reachLimsNo
		except NameError:
			reply = QMessageBox.question(self, '信息', '是否需要获取Reach信息文件', QMessageBox.Yes | QMessageBox.No,
										 QMessageBox.Yes)
			if reply == QMessageBox.Yes:
				MyMainWindow.getReachMessage(self)
				self.textBrowser.setText("请继续点击搜索按钮以搜索Reach信息")
			else:
				self.textBrowser.setText("请点击获取按钮以取得Reach信息")
		else:
			reachContent = self.lineEdit_4.text()
			reachNum = self.spinBox_6.text()
			# print(type(reachContent),1,type(reachNum))
			if (reachContent == '') and (reachNum == '0'):
				self.textBrowser.setText("请输入需要查找Reach英文内容或者编号")
			else:
				m = 'F'
				if reachContent == '':
					for n in range(len(reachLimsNo)):
						if float(reachNum) == float(reachLimsNo[n]):
							m = 'T'
				elif reachNum == '0':
					for n in range(len(reachEnglish)):
						if (reachContent in reachEnglish[n]):
							m = 'T'
				else:  # 两者都不为空时匹配
					for n in range(len(reachEnglish)):
						if (reachContent in reachEnglish[n]) and float(reachNum) == float(reachLimsNo[n]):
							m = 'T'
				# print(m)
				if m == 'T':
					for i in range(len(reachEnglish)):
						# print(reachNum,reachLimsNo[i])
						if reachContent == '':
							if float(reachNum) == float(reachLimsNo[i]):
								self.textBrowser_2.append("Reach Lims No:%s" % reachLimsNo[i])
								self.textBrowser_2.append("Reach 中文名:%s" % reachChinese[i])
								self.textBrowser_2.append("Reach 英文名:%s" % reachEnglish[i])
								self.textBrowser_2.append("Reach CAS No:%s\n" % reachCas[i])
								self.textBrowser_2.append("Reach 物质作用:\n%s" % reachPurpose[i])
								self.textBrowser_2.append('--------------------------')
								self.lineEdit_5.setText("Reach 中文名:%s" % reachChinese[i])
								app.processEvents()
						elif reachNum == '0':
							if reachContent in reachEnglish[i]:
								self.textBrowser_2.append("Reach Lims No:%s" % reachLimsNo[i])
								self.textBrowser_2.append("Reach 中文名:%s" % reachChinese[i])
								self.textBrowser_2.append("Reach 英文名:%s" % reachEnglish[i])
								self.textBrowser_2.append("Reach CAS No:%s\n" % reachCas[i])
								self.textBrowser_2.append("Reach 物质作用:\n%s" % reachPurpose[i])
								self.textBrowser_2.append('--------------------------')
								self.lineEdit_5.setText("Reach 中文名:%s" % reachChinese[i])
								app.processEvents()
						else:
							if (reachContent in reachEnglish[i]) and (float(reachNum) == float(reachLimsNo[i])):
								self.textBrowser_2.append("Reach Lims No:%s" % reachLimsNo[i])
								self.textBrowser_2.append("Reach 中文名:%s" % reachChinese[i])
								self.textBrowser_2.append("Reach 英文名:%s" % reachEnglish[i])
								self.textBrowser_2.append("Reach CAS No:%s\n" % reachCas[i])
								self.textBrowser_2.append("Reach 物质作用:\n%s" % reachPurpose[i])
								self.textBrowser_2.append('--------------------------')
								self.lineEdit_5.setText("Reach 中文名:%s" % reachChinese[i])
								app.processEvents()
				else:
					self.textBrowser_2.append("请确认查找Reach英文内容或者编号是否写对，\n当物质编号不为‘0’和物质内容不为空时，\n物质内容和编号要同时匹配才能查找Reach信息")
					self.textBrowser_2.append('--------------------------')
				self.textBrowser.setText("搜索完成")











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
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	myWin.getConfig()
	sys.exit(app.exec_())