# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Organic_Operate_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Organic_Operate_Ui import *
import chicon  # 引用图标

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.getBatch)
        self.pushButton_3.clicked.connect(self.stopMessage)
        self.pushButton_2.clicked.connect(self.autoWrite)
        self.actionExport.triggered.connect(self.exportConfig)
        self.actionImport.triggered.connect(self.importConfig)
        self.actionExit.triggered.connect(MyMainWindow.close)
        self.actionAuthor.triggered.connect(self.showAuthorMessage)
        self.actionHelp.triggered.connect(self.textBrowser.clear)
        self.pushButton_4.clicked.connect(self.clearContent)
        # QtCore.QMetaObject.connectSlotsByName(MyMainWindow)


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
        configFile = os.path.exists('%s/config_organic.txt' % configFileUrl)
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
        # 获取配置文件内容
        f1 = open('%s/config_organic.txt' % configFileUrl, "r", encoding="utf-8")
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
        configContent = ['默认，可更改为自己需要的', 'Z:\\Organic Batch']
        f1 = open('%s/config_organic.txt' % configFileUrl, "w", encoding="utf-8")
        i = 0
        for i in range(len(configContentName)):
            f1.write(configContentName[i] + '||||||' + configContent[i] + '\n')
            i += 1
        self.textBrowser.append("配置文件创建成功")
        QMessageBox.information(self, "提示信息",
                                "默认配置文件已经创建好，\n如需修改请在用户桌面查找config文件夹中config_organic.txt，\n将相应的文件内容替换成用户需求即可，修改后记得重新导入配置文件。\n切记：中间‘||||||’六根，不能多也不能少！！！",
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


    def getBatch(self):
        self.textBrowser.clear()
        self.lineEdit.clear()
        self.lineEdit.setText('Sample ID')
        global labNumber
        global selectBatchFile
        labNumber = []
        selectBatchFile = QFileDialog.getOpenFileNames(self, '选择Batch文件','%s' % configContent['Organic_Batch_Import_URL'],'Excel files(*.xls*;*.docx;*.csv)')
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
                fileType = os.path.split(file)[1].split('.')[-1]
                self.textBrowser.append('%s:%s' % (n, fileName))
                app.processEvents()
                if 'xls' in fileType:
                    wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % file))
                    ws = wb.Worksheets('sheet1')
                    x = 2
                    while ws.Cells(x, 1).Value is not None:
                        labNumber.append(ws.Cells(x, 1).Value)
                        x += 1

                elif 'doc' in fileType:
                    doc = Document(r"%s" % selectBatchFile[0][n].replace('/', '\\'))
                    for table in doc.tables:
                        for row in table.rows:
                            i = 1
                            for cell in row.cells:
                                if i == 2:
                                    labNumber.append(cell.text)
                                    i += 1
                                    # 去除质控
                                    # if '/' in cell.text:
                                    #     labNumber.append(cell.text)
                                    #     i += 1
                                    # else:
                                    #     # print(cell.text,i)
                                    #     continue
                                else:
                                    i += 1
                elif 'csv' in fileType:
                    batchFile = file.replace('/', '\\')
                    csvFile = pd.read_csv(batchFile)
                    # 去除质控
                    # sampleNum = list(csvFile[' Sample No.'])
                    # leaveNum = []
                    # for each in sampleNum:
                    #     if '/' in each:
                    #         leaveNum.append(each)
                    # csvFile = csvFile.loc[(csvFile[' Sample No.'].isin(leaveNum))]
                    labNumber += list(csvFile[' Sample No.'])
                    app.processEvents()
                n += 1
            if 'xls' in fileType:
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
            velocityNum = float(self.doubleSpinBox.text())
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
                        pyautogui.typewrite('%s' % labNumber[n], velocityNum)
                        pyautogui.typewrite(['Down'])
                        app.processEvents()
                        n += 1
                    elif self.lineEdit.text() == 'stop' or self.lineEdit.text() == 'Stop':
                        break
                self.textBrowser.append('Sample ID填写完成')


if __name__ == "__main__":
    import sys
    import os
    import time
    import pyautogui
    import chicon #引用图标
    import win32com.client as win32com
    import pandas as pd
    from docx import Document
    from win32com.client import Dispatch
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    myWin = MyMainWindow()
    myWin.show()
    myWin.getConfig()
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
