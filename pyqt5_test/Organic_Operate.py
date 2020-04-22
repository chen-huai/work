# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Organic_Operate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 537)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStatusTip("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 5, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 5, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAuthor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        # 需要拷贝数据
        QMessageBox.setWindowIcon(self, icon)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.getBatch)
        self.pushButton_3.clicked.connect(self.stopMessage)
        self.pushButton_2.clicked.connect(self.autoWrite)
        self.actionExport.triggered.connect(self.exportConfig)
        self.actionImport.triggered.connect(self.importConfig)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionAuthor.triggered.connect(self.showAuthorMessage)
        self.actionHelp.triggered.connect(self.textBrowser.clear)
        self.pushButton_4.clicked.connect(self.clearContent)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def getConfig(self):
        # 初始化，获取或生成配置文件
        global configFileUrl
        global desktopUrl
        global now
        global last_time
        global today
        # getBatch里的
        global labNumber
        global selectBatchFile
        now = int(time.strftime('%Y'))
        last_time = now - 1
        today = time.strftime('%Y%m%d')
        desktopUrl = os.path.join(os.path.expanduser("~"), 'Desktop')
        configFileUrl = '%s/config' % desktopUrl
        configFile = os.path.exists('%s/config.txt' % configFileUrl)
        # print(desktopUrl,configFileUrl,configFile)
        if not configFile:  # 判断是否存在文件夹如果不存在则创建为文件夹
            reply = QMessageBox.question(self, '信息', '确认是否要创建配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                if not os.path.exists(configFileUrl):
                    os.makedirs(configFileUrl)
                Ui_MainWindow.createConfigContent(self)
                Ui_MainWindow.getConfigContent(self)
                self.textBrowser.append("创建并导入配置成功")
            else:
                exit()
        else:
            Ui_MainWindow.getConfigContent(self)

    def getConfigContent(self):
        # 获取配置文件内容
        f1 = open('%s/config.txt' % configFileUrl, "r", encoding="utf-8")
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
        self.textBrowser.append("获取配置文件成功")

    def createConfigContent(self):
        # 生成默认配置文件
        configContentName = ['选择Organic_Batch的输入路径和结果输出路径', 'Organic_Batch_Import_URL']
        configContent = ['默认，可更改为自己需要的', 'Z:\\Organic_batch\\Batch']
        f1 = open('%s/config.txt' % configFileUrl, "w", encoding="utf-8")
        i = 0
        for i in range(len(configContentName)):
            f1.write(configContentName[i] + '||||||' + configContent[i] + '\n')
            i += 1
        self.textBrowser.append("配置文件创建成功")
        QMessageBox.information(self, "提示信息",
                                "默认配置文件已经创建好，\n如需修改请在用户桌面查找config文件夹中config.txt，\n将相应的文件内容替换成用户需求即可，修改后记得重新导入配置文件。\n切记：中间‘||||||’六根，不能多也不能少！！！",
                                QMessageBox.Yes)

    def exportConfig(self):
        # 重新导出默认配置文件
        reply = QMessageBox.question(self, '信息', '确认是否要创建默认配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            Ui_MainWindow.createConfigContent(self)
        else:
            QMessageBox.information(self, "提示信息", "没有创建默认配置文件，保留原有的配置文件", QMessageBox.Yes)

    def importConfig(self):
        # 重新导入配置文件
        reply = QMessageBox.question(self, '信息', '确认是否要导入配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            Ui_MainWindow.getConfigContent(self)
        else:
            QMessageBox.information(self, "提示信息", "没有重新导入配置文件，将按照原有的配置文件操作", QMessageBox.Yes)

    def showAuthorMessage(self):
        # 关于作者
        QMessageBox.about(self, "关于",
                          "人生苦短，码上行乐。\n\n\n        ----Frank Chen")

    def getBatch(self):
        self.textBrowser.clear()
        self.lineEdit.clear()
        self.lineEdit.setText('Sample ID')
        global labNumber
        global selectBatchFile
        labNumber = []
        selectBatchFile = QFileDialog.getOpenFileNames(self, '选择Batch文件','%s' % configContent['Organic_Batch_Import_URL'],'Excel files(*.xls*)')
        if selectBatchFile[0] != []:
            self.textBrowser.append('正在获取Sample ID')
            self.textBrowser.append("Sample ID抓取完成后，\n才可以开始下一步骤！！！")
            app.processEvents()
            excel = win32com.gencache.EnsureDispatch('Excel.Application')
            excel.Visible = 0
            excel.Application.DisplayAlerts = True
            n = 1
            for file in selectBatchFile[0]:
                fileName = os.path.split(file)[1]
                self.textBrowser.append('%s:%s' % (n, fileName))
                app.processEvents()
                wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % file))
                ws = wb.Worksheets('sheet1')
                x = 2
                while ws.Cells(x, 1).Value is not None:
                    labNumber.append(ws.Cells(x, 1).Value)
                    x += 1
                n += 1
            excel.Quit()
            self.textBrowser.append('Sample ID抓取完成\n开始填写前，将输入法换成英文输入法！！！！')
        else:
            self.textBrowser.setText("请重新选择Batch文件")


    def clearContent(self):
        # 清除填写内容
        self.lineEdit.clear()
        self.lineEdit.setText("Sample ID")
        self.textBrowser.append("可以开始Sample ID填写")

    def stopMessage(self):
        # 自动填写-停止
        stopMessage = 'Stop'
        self.lineEdit.setText(stopMessage)
        self.textBrowser.append("已停止，请清零后重新开始!!!")

    def autoWrite(self):
        # 自动填写 - 开始自动填写
        if self.lineEdit.text() == '' or self.lineEdit.text() == 'stop' or self.lineEdit.text() == 'Stop':
            QMessageBox.information(self, "提示信息", "自动填写中无内容或内容为‘stop’，请清零并填写内容",
                                    QMessageBox.Yes)
        else:
            time.sleep(3)
            starNum = int(self.spinBox.text())
            endNum = int(self.spinBox_2.text())
            if self.lineEdit.text() == 'Sample ID' or self.lineEdit.text() == 'sample ID':
                self.textBrowser.append("正在填写样品单号")
                app.processEvents()
                if endNum == 0 or endNum > len(labNumber):
                    m = len(labNumber) - starNum + 1
                else:
                    m = endNum - starNum + 1
                n = starNum - 1
                for i in range(m):
                    app.processEvents()
                    time.sleep(0.1)
                    if self.lineEdit.text() == 'Sample ID' or self.lineEdit.text() == 'sample ID':
                        pyautogui.typewrite('%s' % labNumber[n], 0.001)
                        pyautogui.typewrite(['Down'])
                        app.processEvents()
                        n += 1
                    elif self.lineEdit.text() == 'stop' or self.lineEdit.text() == 'Stop':
                        break
                self.textBrowser.append('Sample ID填写完成')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Organic Operate"))
        MainWindow.setStatusTip(_translate("MainWindow", "作者：Frank Chen"))
        self.pushButton_6.setText(_translate("MainWindow", "信息："))
        self.pushButton.setStatusTip(_translate("MainWindow", "选择Batch文件，并获取Sample ID"))
        self.pushButton.setText(_translate("MainWindow", "选择Batch"))
        self.lineEdit.setStatusTip(_translate("MainWindow", "内容为Sample ID时:可以填写；内容为Stop时:无法填写"))
        self.lineEdit.setText(_translate("MainWindow", "Sample ID"))
        self.pushButton_4.setStatusTip(_translate("MainWindow", "清除内容"))
        self.pushButton_4.setText(_translate("MainWindow", "清零"))
        self.textBrowser.setStatusTip(_translate("MainWindow", "消息提示"))
        self.pushButton_8.setText(_translate("MainWindow", "起始编号"))
        self.pushButton_5.setText(_translate("MainWindow", "结尾编号"))
        self.spinBox.setStatusTip(_translate("MainWindow", "起始编号"))
        self.spinBox_2.setStatusTip(_translate("MainWindow", "结尾编号，0默认表示该单号最后一个"))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "停止填写"))
        self.pushButton_3.setText(_translate("MainWindow", "停止填写"))
        self.pushButton_2.setStatusTip(_translate("MainWindow", "点击开始后，3秒时间选择起始位置，并从起始位置开始向下填写单号"))
        self.pushButton_2.setText(_translate("MainWindow", "开始填写"))
        self.pushButton_7.setText(_translate("MainWindow", "自动填写Sample ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Auto"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))

if __name__ == "__main__":
    import sys
    import os
    import time
    import pyautogui
    import chicon #引用图标
    import win32com.client as win32com
    from win32com.client import Dispatch
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    ui.getConfig()
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
