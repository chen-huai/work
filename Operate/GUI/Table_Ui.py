# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TableWindow(object):
    def setupUi(self, TableWindow):
        TableWindow.setObjectName("TableWindow")
        TableWindow.resize(808, 610)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TableWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TableWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        TableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TableWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 22))
        self.menubar.setObjectName("menubar")
        TableWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TableWindow)
        self.statusbar.setObjectName("statusbar")
        TableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TableWindow)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def retranslateUi(self, TableWindow):
        _translate = QtCore.QCoreApplication.translate
        TableWindow.setWindowTitle(_translate("TableWindow", "Data"))
        TableWindow.setStatusTip(_translate("TableWindow", "作者：Frank Chen"))
        self.groupBox.setTitle(_translate("TableWindow", "Reach结果判定界面"))
        self.tableWidget.setStatusTip(_translate("TableWindow", "Reach物质信息"))

