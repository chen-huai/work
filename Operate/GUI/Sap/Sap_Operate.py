import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Sap_Operate_UI import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)

		self.actionExport.triggered.connect(self.exportConfig)
		self.actionImport.triggered.connect(self.importConfig)
		self.actionExit.triggered.connect(MyMainWindow.close)
		self.actionHelp.triggered.connect(self.showVersion)
		self.actionAuthor.triggered.connect(self.showAuthorMessage)
		self.pushButton_11.clicked.connect(self.sapOperate)
		self.pushButton_12.clicked.connect(self.textBrowser.clear)
		# self.pushButton_12.clicked.connect(self.lineEdit.clear)
		# self.pushButton_12.clicked.connect(self.lineEdit.clear)
		# self.pushButton_12.clicked.connect(self.lineEdit.clear)
		# self.pushButton_12.clicked.connect(self.lineEdit.clear)

	def getConfig(self):
		# 初始化，获取或生成配置文件
		global configFileUrl
		global desktopUrl
		global now
		global last_time
		global today

		now = int(time.strftime('%Y'))
		last_time = now - 1
		today = time.strftime('%Y.%m.%d')
		desktopUrl = os.path.join(os.path.expanduser("~"), 'Desktop')
		configFileUrl = '%s/config' % desktopUrl
		configFile = os.path.exists('%s/config_user.csv' % configFileUrl)
		# print(desktopUrl,configFileUrl,configFile)
		if not configFile:  # 判断是否存在文件夹如果不存在则创建为文件夹
			reply = QMessageBox.question(self, '信息', '确认是否要创建配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
			if reply == QMessageBox.Yes:
				if not os.path.exists(configFileUrl):
					os.makedirs(configFileUrl)
				MyMainWindow.createConfigContent(self)
				MyMainWindow.getConfigContent(self)
				self.textBrowser.append("创建并导入配置成功")
			else:
				exit()
		else:
			MyMainWindow.getConfigContent(self)

	def getConfigContent(self):
		csvFile = pd.read_csv('%s/config_user.csv' % configFileUrl, names=['A', 'B', 'C'])
		global configContent
		global username
		global role
		configContent = {}
		username = list(csvFile['A'])
		number = list(csvFile['B'])
		role = list(csvFile['C'])
		for i in range(len(username)):
			configContent['%s' % username[i]] = number[i]
		# a = len(configContent)
		# if (int(configContent['config_num']) != len(configContent)) or (len(configContent) != 40):
		# 	reply = QMessageBox.question(self, '信息', 'config文件配置缺少一些参数，是否重新创建并获取新的config文件', QMessageBox.Yes | QMessageBox.No,
		# 								 QMessageBox.Yes)
		# 	if reply == QMessageBox.Yes:
		# 		MyMainWindow.createConfigContent(self)
		# 		MyMainWindow.getConfigContent(self)
		MyMainWindow.csItem(self)
		MyMainWindow.salesItem(self)
		try:
			self.textBrowser.append("配置获取成功")
		except AttributeError:
			QMessageBox.information(self, "提示信息", "已获取配置文件内容", QMessageBox.Yes)
		else:
			pass

	def createConfigContent(self):
		months = "JanFebMarAprMayJunJulAugSepOctNovDec"
		n = time.strftime('%m')
		pos = (int(n) - 1) * 3
		monthAbbrev = months[pos:pos + 3]

		configContent = [
			['名称','编号','角色'],# getConfigContent()中需要更改配置文件数量
			['chen, frank', '6375108', 'CS'],
			['chen, frank', '6375108', 'Sales'],
		]
		config = np.array(configContent)
		df = pd.DataFrame(config)
		df.to_csv('%s/config_user.csv' % configFileUrl, index=0, header=0, encoding='utf_8_sig')
		self.textBrowser.append("配置文件创建成功")
		QMessageBox.information(self, "提示信息",
								"默认配置文件已经创建好，\n如需修改请在用户桌面查找config文件夹中config_user.csv，\n将相应的文件内容替换成用户需求即可，修改后记得重新导入配置文件。",
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

	def csItem(self):
		self.comboBox_2.clear()
		self.comboBox_2.addItem('')
		nameList = username
		i = 0
		for each in nameList:
			if role[i] == 'CS':
				self.comboBox_2.addItem(each)
			i += 1
			app.processEvents()

	def salesItem(self):
		self.comboBox_3.clear()
		self.comboBox_3.addItem('')
		nameList = username
		i = 0
		for each in nameList:
			if role[i] == 'Sales':
				self.comboBox_3.addItem(each)
			i += 1
			app.processEvents()

	def showAuthorMessage(self):
		# 关于作者
		QMessageBox.about(self, "关于",
						  "人生苦短，码上行乐。\n\n\n        ----Frank Chen")

	def showVersion(self):
		# 关于作者
		QMessageBox.about(self, "版本",
						  "V 22.01.01\n\n\n 2022-03-17")

	def sapOperate(self):
		try:
			SapGuiAuto = win32com.client.GetObject("SAPGUI")
			if not type(SapGuiAuto) == win32com.client.CDispatch:
				return

			application = SapGuiAuto.GetScriptingEngine
			if not type(application) == win32com.client.CDispatch:
				SapGuiAuto = None
				return

			connection = application.Children(0)
			if not type(connection) == win32com.client.CDispatch:
				application = None
				SapGuiAuto = None
				return

			session = connection.Children(0)
			if not type(session) == win32com.client.CDispatch:
				connection = None
				application = None
				SapGuiAuto = None
				return

			# session.findById("wnd[0]").resizeWorkingPane(65, 19, 0)
			# session.findById("wnd[0]/tbar[0]/okcd").text = "mm03"
			# session.findById("wnd[0]").sendVKey(0)
			# session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").Text="9000000000012"
			# session.findById("wnd[0]").sendVKey(0)
			# session.findById("wnd[1]/tbar[0]/btn[0]").press()()
			# session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP02").select()()

			sapNo = self.lineEdit.text()
			projectNo = self.lineEdit_2.text()
			materialCode = self.lineEdit_3.text()
			currencyType = self.comboBox.currentText()
			exchangeRate = float(self.doubleSpinBox.text())
			globalPartnerCode = self.lineEdit_4.text()
			csName = self.comboBox_2.currentText()
			csCode = configContent[csName]
			salesName = self.comboBox_3.currentText()
			orderNo = ''
			proformaNo = ''

			if salesName != '':
				salesCode = configContent[salesName]
			revenue = float(self.doubleSpinBox_2.text())
			cost = float(self.doubleSpinBox_3.text())
			if sapNo == '' or projectNo == '' or materialCode == '' or currencyType == '' or exchangeRate == '' or globalPartnerCode == '' or csName == '' or revenue == 0.00:
				QMessageBox.information(self, "提示信息", "有关键信息未填", QMessageBox.Yes)
			else:
				if ('405' in materialCode) and ("A2" in materialCode):
					chmCost = format((revenue * exchangeRate - cost) * 0.3 * 0.5, '.2f')
					phyCost = format((revenue * exchangeRate - cost) * 0.3 * 0.5, '.2f')
					chmRe = format(revenue * 0.5, '.2f')
					phyRe = format(revenue * 0.5, '.2f')
				elif ('441' in materialCode) and ("A2" in materialCode):
					chmCost = format((revenue * exchangeRate - cost) * 0.3 * 0.8, '.2f')
					phyCost = format((revenue * exchangeRate - cost) * 0.3 * 0.2, '.2f')
					chmRe = format(revenue * 0.8, '.2f')
					phyRe = format(revenue * 0.2, '.2f')
				else:
					chmCost = format((revenue * exchangeRate - cost) * 0.3, '.2f')
					phyCost = format((revenue * exchangeRate - cost) * 0.3, '.2f')
					chmRe = revenue
					phyRe = revenue
				if salesName == '':
					reply = QMessageBox.question(self, '信息', 'Sales未填，是否继续', QMessageBox.Yes | QMessageBox.No,
												 QMessageBox.Yes)
				if salesName != '' or reply == QMessageBox.Yes:
					self.textBrowser.append("Sap No.:%s" % sapNo)
					self.textBrowser.append("Project No.:%s" % projectNo)
					self.textBrowser.append("materialCode:%s" % materialCode)
					self.textBrowser.append("globalPartnerCode:%s" % globalPartnerCode)
					self.textBrowser.append("csName:%s" % csName)
					self.textBrowser.append("salesName:%s" % salesName)
					self.textBrowser.append("revenue:%s" % revenue)
					self.textBrowser.append("cost:%s" % cost)
					self.textBrowser.append("currencyType:%s" % currencyType)
					self.textBrowser.append("CHM Cost:%s" % chmCost)
					self.textBrowser.append("PHY Cost:%s" % phyCost)
					self.textBrowser.append("CHM revenue:%s" % chmRe)
					self.textBrowser.append("PHY revenue:%s" % phyRe)
					app.processEvents()
					# session.findById("wnd[0]").resizeWorkingPane(172, 38, 0)
					if self.checkBox.isChecked():
						session.findById("wnd[0]/tbar[0]/okcd").text = "/nva01"
						session.findById("wnd[0]").sendVKey(0)
						session.findById("wnd[0]").sendVKey(0)
						session.findById(
							"wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/subPART-SUB:SAPMV45A:4701/ctxtKUAGV-KUNNR").text = sapNo
						session.findById(
							"wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/subPART-SUB:SAPMV45A:4701/ctxtKUAGV-KUNNR").caretPosition = 6
						session.findById("wnd[0]").sendVKey(0)
						session.findById("wnd[0]").sendVKey(0)
						session.findById("wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/txtVBKD-BSTKD").text = projectNo
						session.findById("wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/ctxtVBKD-BSTDK").text = today
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/ctxtVBKD-FBUDA").text = today
						session.findById("wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/txtVBKD-BSTKD").setFocus()
						session.findById("wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/txtVBKD-BSTKD").caretPosition = 17
						session.findById("wnd[0]").sendVKey(0)
						session.findById("wnd[1]/tbar[0]/btn[0]").press()
						session.findById("wnd[0]/usr/subSUBSCREEN_HEADER:SAPMV45A:4021/btnBT_HEAD").press()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:4301/ctxtVBAK-WAERK").text = currencyType
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:4301/ctxtVBAK-WAERK").setFocus()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:4301/ctxtVBAK-WAERK").caretPosition = 3
						session.findById("wnd[0]").sendVKey(0)
						if currencyType != "CNY":
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:4301/ctxtVBKD-KURSK").text = exchangeRate
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:4301/ctxtVBKD-KURSK").setFocus()
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:4301/ctxtVBKD-KURSK").caretPosition = 8
							session.findById("wnd[0]").sendVKey(0)
						session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09").select()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,4]").text = globalPartnerCode
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,4]").setFocus()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,4]").caretPosition = 8
						session.findById("wnd[0]").sendVKey(0)
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,5]").text = csCode
						session.findById("wnd[0]").sendVKey(0)
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/cmbGVS_TC_DATA-REC-PARVW[0,6]").key = "AP"
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,6]").setFocus()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,6]").caretPosition = 0
						session.findById("wnd[0]").sendVKey(4)
						session.findById("wnd[1]/tbar[0]/btn[0]").press()
						session.findById("wnd[1]/tbar[0]/btn[0]").press()
						session.findById("wnd[0]").sendVKey(0)
						if salesName != '':
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/cmbGVS_TC_DATA-REC-PARVW[0,7]").key = "VE"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,7]").text = salesCode
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,7]").setFocus()
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\09/ssubSUBSCREEN_BODY:SAPMV45A:4352/subSUBSCREEN_PARTNER_OVERVIEW:SAPLV09C:1000/tblSAPLV09CGV_TC_PARTNER_OVERVIEW/ctxtGVS_TC_DATA-REC-PARTNER[1,7]").caretPosition = 4
							session.findById("wnd[0]").sendVKey(0)
						session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\10").select()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\10/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[1]/shell").text = "Testing Fee"
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\10/ssubSUBSCREEN_BODY:SAPMV45A:4152/subSUBSCREEN_TEXT:SAPLV70T:2100/cntlSPLITTER_CONTAINER/shellcont/shellcont/shell/shellcont[1]/shell").setSelectionIndexes(
							11, 11)
						session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\13").select()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\13/ssubSUBSCREEN_BODY:SAPMV45A:4309/cmbVBAK-KVGR1").key = "00"
						session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14").select()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/ctxtVBAK-ZZAUART").text = "WO"
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/ctxtVBAK-ZZUNLIMITLIAB").text = "N"
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/ctxtZAUFTD-VORAUS_AUFENDE").text = today
						if 'A2' in materialCode:
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AZULEISTENDE/ctxtTABL-KOSTL[0,0]").text = "48601293"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AZULEISTENDE/ctxtTABL-KOSTL[0,1]").text = "48601294"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/ctxtTABD-KOSTL[0,0]").text = "48601293"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/ctxtTABD-KOSTL[0,1]").text = "48601294"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/txtTABD-FESTPREIS[5,0]").text = chmCost
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/txtTABD-FESTPREIS[5,1]").text = phyCost
						elif 'T20' in materialCode:
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AZULEISTENDE/ctxtTABL-KOSTL[0,0]").text = "48601294"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/ctxtTABD-KOSTL[0,0]").text = "48601294"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/txtTABD-FESTPREIS[5,0]").text = phyCost
						else:
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AZULEISTENDE/ctxtTABL-KOSTL[0,0]").text = "48601293"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/ctxtTABD-KOSTL[0,0]").text = "48601293"
							session.findById(
								"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AKOSTENSAETZE/txtTABD-FESTPREIS[5,0]").text = chmCost

						session.findById("wnd[0]").sendVKey(0)
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AZULEISTENDE/ctxtTABL-KOSTL[0,1]").setFocus()
						session.findById(
							"wnd[0]/usr/tabsTAXI_TABSTRIP_HEAD/tabpT\\14/ssubSUBSCREEN_BODY:SAPMV45A:4312/tblSAPMV45AZULEISTENDE/ctxtTABL-KOSTL[0,1]").caretPosition = 8

						if self.checkBox_2.isChecked():
							session.findById("wnd[0]/tbar[0]/btn[3]").press()
							session.findById("wnd[0]/tbar[0]/btn[3]").press()
							session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
							# session.findById("wnd[0]/tbar[0]/btn[11]").press
							# session.findById("wnd[1]/usr/btnSPOP-OPTION1").press

					if self.checkBox_2.isChecked():
							session.findById("wnd[0]/tbar[0]/okcd").text = "/NVA02"
							session.findById("wnd[0]").sendVKey(0)
							orderNo = session.findById("wnd[0]/usr/ctxtVBAK-VBELN").text
							session.findById("wnd[0]").sendVKey(0)
							if ('A2' in materialCode) and ('405' in materialCode):
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").text = "T75-405-00"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,1]").text = "T20-405-00"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,0]").text = "1"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,1]").text = "1"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtVBAP-ZIEME[3,0]").text = "pu"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtVBAP-ZIEME[3,1]").text = "pu"
								session.findById("wnd[0]").sendVKey(0)
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").caretPosition = 10
								session.findById("wnd[0]").sendVKey(2)
								session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06").select()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").text = chmRe
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").caretPosition = 16
								session.findById("wnd[0]").sendVKey(0)
								session.findById("wnd[0]/tbar[0]/btn[3]").press()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,1]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,1]").caretPosition = 16
								session.findById("wnd[0]").sendVKey(2)
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").text = phyRe
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").caretPosition = 16
								session.findById("wnd[0]/tbar[0]/btn[3]").press()
							elif ('A2' in materialCode) and ('441' in materialCode):
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").text = "T75-441-00"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,1]").text = "T20-441-00"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,0]").text = "1"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,1]").text = "1"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtVBAP-ZIEME[3,0]").text = "pu"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtVBAP-ZIEME[3,1]").text = "pu"
								session.findById("wnd[0]").sendVKey(0)
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").caretPosition = 10
								session.findById("wnd[0]").sendVKey(2)
								session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06").select()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").text = chmRe
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").caretPosition = 16
								session.findById("wnd[0]").sendVKey(0)
								session.findById("wnd[0]/tbar[0]/btn[3]").press()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,1]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,1]").caretPosition = 16
								session.findById("wnd[0]").sendVKey(2)
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").text = phyRe
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").caretPosition = 16
								session.findById("wnd[0]/tbar[0]/btn[3]").press()
							elif 'T20' in materialCode:
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").text = "T20-405-00"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,0]").text = "1"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtVBAP-ZIEME[3,0]").text = "pu"
								session.findById("wnd[0]").sendVKey(0)
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").caretPosition = 10
								session.findById("wnd[0]").sendVKey(2)
								session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06").select()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").text = revenue
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").caretPosition = 16
								session.findById("wnd[0]").sendVKey(0)
								session.findById("wnd[0]/tbar[0]/btn[3]").press()
							else:
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").text = "T75-405-00"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/txtVBAP-ZMENG[2,0]").text = "1"
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtVBAP-ZIEME[3,0]").text = "pu"
								session.findById("wnd[0]").sendVKey(0)
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\02/ssubSUBSCREEN_BODY:SAPMV45A:4415/subSUBSCREEN_TC:SAPMV45A:4902/tblSAPMV45ATCTRL_U_ERF_GUTLAST/ctxtRV45A-MABNR[1,0]").caretPosition = 10
								session.findById("wnd[0]").sendVKey(2)
								session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06").select()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").text = revenue
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").setFocus()
								session.findById(
									"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\06/ssubSUBSCREEN_BODY:SAPLV69A:6201/tblSAPLV69ATCTRL_KONDITIONEN/txtKOMV-KBETR[3,5]").caretPosition = 16
								session.findById("wnd[0]").sendVKey(0)
								session.findById("wnd[0]/tbar[0]/btn[3]").press()
							if self.checkBox_3.isChecked():
								session.findById("wnd[0]/tbar[0]/btn[3]").press()
								session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
								session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
								# session.findById("wnd[0]/tbar[0]/btn[11]").press
								# session.findById("wnd[1]/usr/btnSPOP-OPTION1").press

					if self.checkBox_3.isChecked():
						session.findById("wnd[0]/tbar[0]/okcd").text = "/nvf01"
						session.findById("wnd[0]").sendVKey(0)
						session.findById("wnd[0]/tbar[0]/btn[11]").press()

					if self.checkBox_4.isChecked():
						session.findById("wnd[0]/tbar[0]/okcd").text = "/nvf03"
						session.findById("wnd[0]").sendVKey(0)
						proformaNo = session.findById("wnd[0]/usr/ctxtVBRK-VBELN").text
						session.findById("wnd[0]/mbar/menu[0]/menu[11]").select()
						session.findById("wnd[1]/tbar[0]/btn[37]").press()
					if orderNo:
						self.textBrowser.append("Order No.:%s" % orderNo)
					if proformaNo:
						self.textBrowser.append("Proforma No.:%s" % proformaNo)
					self.textBrowser.append('SAP操作已完成')
					self.textBrowser.append('----------------------------------')
					app.processEvents()

		except:
			self.textBrowser.append('SAP有问题')
			self.textBrowser.append(sys.exc_info()[0])
			# print(sys.exc_info()[0])

		finally:
			session = None
			connection = None
			application = None
			SapGuiAuto = None
if __name__ == "__main__":
	import sys
	import os
	import time
	import win32com.client
	import pandas as pd
	import numpy as np
	import re
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	myWin.getConfig()
	sys.exit(app.exec_())