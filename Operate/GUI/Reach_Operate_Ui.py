# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reach_Operate_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 616)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.spinBox_1 = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_1.sizePolicy().hasHeightForWidth())
        self.spinBox_1.setSizePolicy(sizePolicy)
        self.spinBox_1.setMaximum(999999999)
        self.spinBox_1.setObjectName("spinBox_1")
        self.gridLayout.addWidget(self.spinBox_1, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 2, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(2, "")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(2, "")
        self.gridLayout.addWidget(self.comboBox_3, 2, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.gridLayout.addWidget(self.comboBox_4, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/message.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/message.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/message.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/message.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/message.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/message.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/message.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(150, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icon/clean.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_1.setIcon(icon2)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_3.addWidget(self.pushButton_1, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/search.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.actionExport.setIcon(icon4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionExport.setFont(font)
        self.actionExport.setIconVisibleInMenu(True)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/exit.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.actionImport = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap(":/import.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/import.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap(":/import.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/import.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap(":/import.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/import.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.actionImport.setIcon(icon6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionImport.setFont(font)
        self.actionImport.setIconVisibleInMenu(True)
        self.actionImport.setObjectName("actionImport")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(":/help.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.actionHelp.setIcon(icon7)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("icon/author.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.actionAuthor.setIcon(icon8)
        self.actionAuthor.setObjectName("actionAuthor")
        self.menu.addAction(self.actionExport)
        self.menu.addAction(self.actionImport)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAuthor)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "操作界面"))
        MainWindow.setStatusTip(_translate("MainWindow", "作者：Frank Chen"))
        self.groupBox_2.setTitle(_translate("MainWindow", "信息筛选"))
        self.pushButton_4.setText(_translate("MainWindow", "物质编号"))
        self.pushButton_5.setText(_translate("MainWindow", "CAS NO."))
        self.spinBox_1.setStatusTip(_translate("MainWindow", "输入Lims中的Reach物质编号"))
        self.pushButton.setText(_translate("MainWindow", "英文名称"))
        self.lineEdit_1.setStatusTip(_translate("MainWindow", "输入Reach物质的英文内容"))
        self.pushButton_6.setText(_translate("MainWindow", "物质分类"))
        self.comboBox_2.setStatusTip(_translate("MainWindow", "选择物质类型"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Natural textiles"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Synthetic textiles"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Leather"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Metal"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Plastic|polymers|foam"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Wood"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Paper"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Ceramic "))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Glass"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Dye|Pigment|Ink|Paint"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Adhesives|Sealants"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Battery"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Electronic components"))
        self.pushButton_7.setText(_translate("MainWindow", "项目分类"))
        self.comboBox.setStatusTip(_translate("MainWindow", "选择项目类型"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Inorganic"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Organic"))
        self.pushButton_9.setText(_translate("MainWindow", "风险评估"))
        self.comboBox_3.setStatusTip(_translate("MainWindow", "选择风险，Y-高风险，N-低风险"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Y"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "N"))
        self.comboBox_4.setStatusTip(_translate("MainWindow", "选择Cas No.化学物质编号"))
        self.groupBox_4.setTitle(_translate("MainWindow", "表现形式"))
        self.checkBox.setStatusTip(_translate("MainWindow", "以表格形式显示查询信息"))
        self.checkBox.setText(_translate("MainWindow", "表格"))
        self.checkBox_2.setStatusTip(_translate("MainWindow", "以文本形式显示查询信息"))
        self.checkBox_2.setText(_translate("MainWindow", "文本"))
        self.groupBox_3.setTitle(_translate("MainWindow", "操作"))
        self.pushButton_2.setStatusTip(_translate("MainWindow", "获取Reach物质信息"))
        self.pushButton_2.setText(_translate("MainWindow", "获取所有信息"))
        self.pushButton_1.setStatusTip(_translate("MainWindow", "将所有之前查找的信息清除"))
        self.pushButton_1.setText(_translate("MainWindow", "清零"))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "根据内容或编号查找Reach物质的信息"))
        self.pushButton_3.setText(_translate("MainWindow", "显示信息"))
        self.groupBox.setTitle(_translate("MainWindow", "查询Reach物质信息显示区域"))
        self.textBrowser.setStatusTip(_translate("MainWindow", "信息显示框"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Reach Message"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExport.setToolTip(_translate("MainWindow", "Export"))
        self.actionExport.setStatusTip(_translate("MainWindow", "导出默认配置信息，可在用户桌面config文件夹中查看"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "退出程序"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionImport.setStatusTip(_translate("MainWindow", "导入配置文件，当配置文件修改时请使用，配置文件可在用户桌面config文件夹中找到"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "帮助提示"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))
        self.actionAuthor.setStatusTip(_translate("MainWindow", "关于作者"))
