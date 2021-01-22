import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import chicon  # 引用图标
from Reach_Operate_Ui import *
from TableView_Ui import *

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
		configContentName = ['选择ICP_Batch的输入路径和结果输出路径', 'Reach_Message_Import_URL','Reach_Message_File_Name']
		configContent = ['默认，可更改为自己需要的','Z:\\Inorganic\\Program\\1.Inorganic Operate\\1.New edition\\2.Model', 'REACH_SVHC_Candidate_List_Opinion.csv']
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
		global reachMessage
		global searchReachMessage
		file = configContent['Reach_Message_Import_URL'] + '\\' + configContent['Reach_Message_File_Name']
		folder = os.path.exists(file)
		if not folder:
			QMessageBox.information(self, "无Reach信息模板",
									"没有Reach信息文件！！！\n请查看config_reach配置文件内容是否符合需求。\nReach_Message_Import_URL,Reach_Message_File_Name\nReach Message的文件路径、文件名称和CSV格式",
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
			
			reachContent = self.lineEdit_1.text()
			reachNum = self.spinBox_1.text()
			casNum = self.lineEdit.text()
			# 只要物质信息的搜索
			if (reachContent == '') and (reachNum == 0) and (casNum == ''):

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
									self.textBrowser.append("Reach Lims No:%s" % reachLimsNo[i])
									self.textBrowser.append("Reach 中文名:%s" % reachChinese[i])
									self.textBrowser.append("Reach 英文名:%s" % reachEnglish[i])
									self.textBrowser.append("Reach CAS No:%s\n" % reachCas[i])
									self.textBrowser.append("Reach 物质作用:\n%s" % reachPurpose[i])
									self.textBrowser.append('--------------------------')
									self.lineEdit_5.setText("Reach 中文名:%s" % reachChinese[i])
									app.processEvents()
							elif reachNum == '0':
								if reachContent in reachEnglish[i]:
									self.textBrowser.append("Reach Lims No:%s" % reachLimsNo[i])
									self.textBrowser.append("Reach 中文名:%s" % reachChinese[i])
									self.textBrowser.append("Reach 英文名:%s" % reachEnglish[i])
									self.textBrowser.append("Reach CAS No:%s\n" % reachCas[i])
									self.textBrowser.append("Reach 物质作用:\n%s" % reachPurpose[i])
									self.textBrowser.append('--------------------------')
									self.lineEdit_5.setText("Reach 中文名:%s" % reachChinese[i])
									app.processEvents()
							else:
								if (reachContent in reachEnglish[i]) and (float(reachNum) == float(reachLimsNo[i])):
									self.textBrowser.append("Reach Lims No:%s" % reachLimsNo[i])
									self.textBrowser.append("Reach 中文名:%s" % reachChinese[i])
									self.textBrowser.append("Reach 英文名:%s" % reachEnglish[i])
									self.textBrowser.append("Reach CAS No:%s\n" % reachCas[i])
									self.textBrowser.append("Reach 物质作用:\n%s" % reachPurpose[i])
									self.textBrowser.append('--------------------------')
									self.lineEdit_5.setText("Reach 中文名:%s" % reachChinese[i])
									app.processEvents()
					else:
						self.textBrowser.append("请确认查找Reach英文内容或者编号是否写对，\n当物质编号不为‘0’和物质内容不为空时，\n物质内容和编号要同时匹配才能查找Reach信息")
						self.textBrowser.append('--------------------------')
					self.textBrowser.setText("搜索完成")
			else:
				global material,project,estimate
				# 物质选择
				material = self.comboBox_2.currentText()
				# 项目选择
				project = self.comboBox.currentText()
				# 风险选择
				estimate = self.comboBox_3.currentText()
				myTable.searchReachMessage()



class MyTableWindow(QMainWindow, Ui_TableWindow):
	def __init__(self, parent=None):
		super(MyTableWindow, self).__init__(parent)
		self.setupUi(self)

	def searchReachMessage(self):
		dropC = ['No.','列入日期','EC 号码','Possible Applications','*Remarks','Chemical Classification']
		maybeC = ['Natural textiles','Synthetic textiles','Leather','Metal','Plastic|polymers|foam','Wood','Paper','Ceramic ','Glass','Dye|Pigment|Ink|Paint','Adhesives|Sealants','Battery','Electronic components','Organic|Inorganic']
		leaveC = ['Lims No.','物质名称(英文)','物质名称(中文)','CAS 号码','可能用途']
		csvHead = list(reachMessage.head())
		if (material == '') and (project == '') and (estimate == ''):
			# 全显示
			pass
		else:
			# 选择性显示
			if material != '':
				maybeC.remove(material)
			if project != '':
				maybeC.remove('Organic|Inorganic')
			dropC += maybeC
			searchReachMessage = reachMessage.drop(dropC, axis=1)
			csvHead = list(searchReachMessage.head())
			csvl = searchReachMessage.index
			res = pd.DataFrame(searchReachMessage,index=csvl,columns=csvHead)
			model = TableModel(res)

			# # 测试
			# data = {'性别': ['男', '女', '女', '男', '男'],
			# 		'姓名': ['小明', '小红', '小芳', '小强', '小美'],
			# 		'年龄': [20, 21, 25, 24, 29]}
			# df = pd.DataFrame(data, index=['No.1', 'No.2', 'No.3', 'No.4', 'No.5'],
			# 				  columns=['姓名', '性别', '年龄', '职业'])
			#
			# model = TableModel(df)

			self.tableView.setModel(model)
			self.tableView.setAlternatingRowColors(True)
			myTable.show()

# 将数据转换为table显示数据
class TableModel(QAbstractTableModel):
	# def __init__(self, data):
	# 	super(TableModel, self).__init__()
	# 	self._data = data
	#
	# def data(self, index, role):
	# 	if role == Qt.DisplayRole:
	# 		# See below for the nested-list data structure.
	# 		# .row() indexes into the outer list,
	# 		# .column() indexes into the sub-list
	# 		return self._data[index.row()][index.column()]
	#
	# def rowCount(self, index):
	# 	# The length of the outer list.
	# 	return len(self._data)
	#
	# def columnCount(self, index):
	# 	# The following takes the first sub-list, and returns
	# 	# the length (only works if all rows are an equal length)
	# 	return len(self._data)
	

	# 测试1
	def __init__(self, data):
		QAbstractTableModel.__init__(self)
		self._data = data

	def rowCount(self, parent=None):
		return self._data.shape[0]

	def columnCount(self, parent=None):
		return self._data.shape[1]

	# 显示数据
	def data(self, index, role=Qt.DisplayRole):
		if index.isValid():
			if role == Qt.DisplayRole:
				return str(self._data.iloc[index.row(), index.column()])
		return None
	
	
	# # 测试2
	# def __init__(self, data):
	# 	QAbstractTableModel.__init__(self)
	# 	self._data = data
	#
	# def toDataFrame(self):
	# 	return self._data.copy()
	#
	# def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
	# 	if role != QtCore.Qt.DisplayRole:
	# 		return QtCore.QVariant()
	#
	# 	if orientation == QtCore.Qt.Horizontal:
	# 		try:
	# 			return self._data.columns.tolist()[section]
	# 		except (IndexError,):
	# 			return QtCore.QVariant()
	# 	elif orientation == QtCore.Qt.Vertical:
	# 		try:
	# 			# return self.df.index.tolist()
	# 			return self._data.index.tolist()[section]
	# 		except (IndexError,):
	# 			return QtCore.QVariant()
	#
	# def data(self, index, role=QtCore.Qt.DisplayRole):
	# 	if role != QtCore.Qt.DisplayRole:
	# 		return QtCore.QVariant()
	#
	# 	if not index.isValid():
	# 		return QtCore.QVariant()
	#
	# 	return QtCore.QVariant(str(self._data.ix[index.row(), index.column()]))
	#
	# def setData(self, index, value, role):
	# 	row = self._data.index[index.row()]
	# 	col = self._data.columns[index.column()]
	# 	if hasattr(value, 'toPyObject'):
	# 		# PyQt4 gets a QVariant
	# 		value = value.toPyObject()
	# 	else:
	# 		# PySide gets an unicode
	# 		dtype = self._data[col].dtype
	# 		if dtype != object:
	# 			value = None if value == '' else dtype.type(value)
	# 	self._data.set_value(row, col, value)
	# 	return True
	#
	# def rowCount(self, parent=QtCore.QModelIndex()):
	# 	return len(self._data.index)
	#
	# def columnCount(self, parent=QtCore.QModelIndex()):
	# 	return len(self._data.columns)
	#
	# def sort(self, column, order):
	# 	colname = self._data.columns.tolist()[column]
	# 	self.layoutAboutToBeChanged.emit()
	# 	self._data.sort_values(colname, ascending=order == QtCore.Qt.AscendingOrder, inplace=True)
	# 	self._data.reset_index(inplace=True, drop=True)
	# 	self.layoutChanged.emit()

if __name__ == "__main__":
	import sys
	import os
	import time
	import pandas as pd
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myTable = MyTableWindow()
	myWin.show()
	myWin.getConfig()
	sys.exit(app.exec_())