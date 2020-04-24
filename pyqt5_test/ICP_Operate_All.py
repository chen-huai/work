# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ICP_Operate_All.ui'
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
        MainWindow.resize(534, 442)
        global icon
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab)
        self.pushButton_28.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_2.addWidget(self.pushButton_28, 0, 0, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_2.addWidget(self.pushButton_29, 0, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setToolTip("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 0, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setToolTip("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.pushButton_23, 0, 3, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_2.addWidget(self.textBrowser_3, 1, 0, 4, 2)
        self.pushButton_24 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setToolTip("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_2.addWidget(self.pushButton_24, 1, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setToolTip("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_2.addWidget(self.pushButton_25, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 2, 1, 2)
        self.pushButton_35 = QtWidgets.QPushButton(self.tab)
        self.pushButton_35.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_2.addWidget(self.pushButton_35, 4, 2, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.tab)
        self.pushButton_36.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_2.addWidget(self.pushButton_36, 4, 3, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.tab)
        self.pushButton_33.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_2.addWidget(self.pushButton_33, 5, 0, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_2.addWidget(self.pushButton_34, 5, 1, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setToolTip("")
        self.spinBox_3.setMaximum(999999999)
        self.spinBox_3.setProperty("value", 1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_2.addWidget(self.spinBox_3, 5, 2, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setToolTip("")
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 5, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 6, 0, 3, 2)
        self.pushButton_38 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setToolTip("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_2.addWidget(self.pushButton_38, 6, 2, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setToolTip("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_2.addWidget(self.pushButton_27, 6, 3, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_2.addWidget(self.pushButton_31, 7, 2, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_2.addWidget(self.pushButton_30, 7, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 8, 2, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_2.addWidget(self.pushButton_32, 8, 3, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setToolTip("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 1, 3, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spinBox_6 = QtWidgets.QSpinBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy)
        self.spinBox_6.setMaximum(999999999)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_3.addWidget(self.spinBox_6, 0, 3, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_40.setEnabled(False)
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_3.addWidget(self.pushButton_40, 0, 2, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_3.addWidget(self.textBrowser_2, 2, 0, 1, 4)
        self.pushButton_37 = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_3.addWidget(self.pushButton_37, 1, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 0, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_3.addWidget(self.pushButton_51, 1, 1, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_3.addWidget(self.pushButton_50, 1, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_19.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_20.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 5, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 5, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 5, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 1, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 1, 3, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 0, 4, 2, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setToolTip("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 5, 3, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy)
        self.spinBox_5.setMaximum(999999999)
        self.spinBox_5.setProperty("value", 3)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout.addWidget(self.spinBox_5, 4, 3, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setMaximum(999999999)
        self.spinBox_4.setProperty("value", 1)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout.addWidget(self.spinBox_4, 3, 3, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_26.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_26, 2, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setToolTip("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setToolTip("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 4, 2, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_44 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayout_5.addWidget(self.pushButton_44, 0, 3, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_5.addWidget(self.textBrowser_4, 1, 0, 2, 2)
        self.line_3 = QtWidgets.QFrame(self.tab_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 0, 2, 3, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_39.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_5.addWidget(self.pushButton_39, 0, 0, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_5.addWidget(self.pushButton_41, 0, 1, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout_5.addWidget(self.pushButton_48, 8, 3, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setObjectName("pushButton_45")
        self.gridLayout_5.addWidget(self.pushButton_45, 2, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 3, 0, 1, 4)
        self.pushButton_42 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_42.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout_5.addWidget(self.pushButton_42, 4, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_5.addWidget(self.line_4, 4, 2, 5, 1)
        self.pushButton_43 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_5.addWidget(self.pushButton_43, 4, 1, 1, 1)
        self.pushButton_46 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout_5.addWidget(self.pushButton_46, 1, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_2, 4, 3, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout_5.addWidget(self.textBrowser_5, 5, 0, 4, 2)
        self.pushButton_47 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout_5.addWidget(self.pushButton_47, 5, 3, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_5.addWidget(self.pushButton_49, 6, 3, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout_5.addWidget(self.pushButton_52, 7, 3, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 22))
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
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionExport.setFont(font)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionImport = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionImport.setFont(font)
        self.actionImport.setObjectName("actionImport")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
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

        # 需要拷贝部分
        QFileDialog.setWindowIcon(self, icon)
        QMessageBox.setWindowIcon(self, icon)
        QInputDialog.setWindowIcon(self, icon)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_23.clicked.connect(self.aasBatch)
        self.pushButton_24.clicked.connect(self.ecoZxd)
        self.pushButton_26.clicked.connect(self.randomAction)
        self.pushButton_27.clicked.connect(self.icpResultToTxt)
        self.pushButton_30.clicked.connect(self.icpQc)
        self.pushButton_22.clicked.connect(self.nickelBatch)
        self.pushButton_25.clicked.connect(self.ecoZjy)
        self.pushButton_29.clicked.connect(lambda: self.getBatch('ICP'))
        self.pushButton_41.clicked.connect(lambda: self.getBatch('UV'))
        self.pushButton_21.clicked.connect(self.icpBatch)
        self.pushButton_34.clicked.connect(lambda: self.getResult('ICP'))
        self.pushButton_43.clicked.connect(lambda: self.getResult('UV'))
        self.pushButton_31.clicked.connect(self.zjyResultToIcp)
        self.pushButton_32.clicked.connect(self.resultZjyToTxt)
        self.pushButton_38.clicked.connect(self.reachResult)
        self.pushButton_39.clicked.connect(self.tabWidget.close)
        self.pushButton_7.clicked.connect(lambda: self.getData(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.getData(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.getData(self.pushButton_9))
        self.pushButton_13.clicked.connect(lambda: self.getData(self.pushButton_13))
        self.pushButton_4.clicked.connect(lambda: self.getData(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.getData(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.getData(self.pushButton_6))
        self.pushButton_14.clicked.connect(lambda: self.getData(self.pushButton_14))
        self.pushButton_10.clicked.connect(lambda: self.getData(self.pushButton_10))
        self.pushButton_2.clicked.connect(lambda: self.getData(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.getData(self.pushButton_3))
        self.pushButton_15.clicked.connect(self.clearContent)
        self.pushButton_11.clicked.connect(lambda: self.getData(self.pushButton_11))
        self.pushButton_12.clicked.connect(lambda: self.getData(self.pushButton_12))
        self.pushButton_17.clicked.connect(lambda: self.getData(self.pushButton_17))
        self.pushButton_18.clicked.connect(lambda: self.getBatch('Auto'))
        self.pushButton.clicked.connect(self.autoWrite)
        self.pushButton_16.clicked.connect(self.stopMessage)
        self.actionExport.triggered.connect(self.exportConfig)
        self.actionImport.triggered.connect(self.importConfig)
        self.actionExit.triggered.connect(MainWindow.close)
        self.pushButton_37.clicked.connect(self.searchReachMessage)
        self.actionImport.triggered.connect(self.lineEdit.clear)
        self.actionHelp.triggered.connect(self.lineEdit.clear)
        self.actionAuthor.triggered.connect(self.showAuthorMessage)
        self.pushButton_50.clicked.connect(self.getReachMessage)
        self.pushButton_51.clicked.connect(self.formalBatch)
        self.pushButton_44.clicked.connect(self.formalBatch)
        self.pushButton_46.clicked.connect(self.crBatch)
        self.pushButton_45.clicked.connect(self.phBatch)
        self.pushButton_47.clicked.connect(lambda: self.uvQc('Formal'))
        self.pushButton_49.clicked.connect(lambda: self.uvQc('Cr VI'))
        self.pushButton_52.clicked.connect(lambda: self.phQc('pH 2018'))
        self.pushButton_48.clicked.connect(lambda: self.phQc('pH 2014'))
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
        global qualityValue
        global volumeValue
        global analyteList
        global batchNum
        global selectBatchFile
        # getResult里的
        global selectResultFile
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
        configFile = os.path.exists('%s/config.txt' % configFileUrl)
        # print(desktopUrl,configFileUrl,configFile)
        if not configFile:  # 判断是否存在文件夹如果不存在则创建为文件夹
            reply = QMessageBox.question(self, '信息', '确认是否要创建配置文件', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                if not os.path.exists(configFileUrl):
                    os.makedirs(configFileUrl)
                Ui_MainWindow.createConfigContent(self)
                Ui_MainWindow.getConfigContent(self)
                self.lineEdit_6.setText("创建并导入配置成功")
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
        self.lineEdit_6.setText("配置获取成功")

    def createConfigContent(self):
        # 生成默认配置文件
        configContentName = ['选择ICP_Batch的输入路径和结果输出路径', 'ICP_Batch_Import_URL', 'ICP_Batch_Export_URL',
                             'ECO_Batch_Export_URL', 'Nickel_Batch_Export_URL', 'Nickel_Batch_Import_URL',
                             'Nickel_File_Name',
                             '选择ICP_Result的输入路径和结果输出路径', 'ICP_Result_Import_URL', 'ICP_Result_Export_URL',
                             'AAS_Result_Import_URL',
                             'AAS_Result_Export_URL', 'ECO_Result_Import_URL', 'ECO_Result_Export_URL',
                             'ICP_QC_Chart_Import_URL',
                             'ICP_QC_Chart_File_Name', 'Reach_Result_Import_URL', 'Reach_Result_File_Name',
                             'Reach_Result_Export_URL',
                             'Reach_Message_Import_URL', 'Reach_Message_File_Name', '选择UV_Batch的输入路径和结果输出路径',
                             'UV_Batch_Import_URL', 'UV_Batch_Export_URL', 'UV_Rusult_Export_URL',
                             '选择UV_Result的输入路径和结果输出路径', 'UV_QC_Chart_Import_URL', 'Formal_QC_Chart_File_Name',
                             'Cr_VI_QC_Chart_File_Name', 'pH2014_QC_Chart_File_Name', 'pH2018_QC_Chart_File_Name',
                             'Formal_Result_Import_URL', 'Cr_VI_Result_Import_URL', 'pH2014_Result_Import_URL',
                             'pH2018_Result_Import_URL']
        configContent = ['默认，可更改为自己需要的', 'Z:\\Inorganic_batch\\Microwave\\Batch', '%s' % desktopUrl,
                         'Z:\\Inorganic_batch\\Microwave\\Result\\ECO',
                         'Z:\\Inorganic_batch\\Microwave\\Result\\Nickel',
                         'Z:\\Inorganic_batch\\Microwave\\Result\\Nickel', 'TC_XMN_CHM_F_T.02E.xlsm', '有条件最好改为跟默认配置一致',
                         'Z:\\Data\\%s\\66-01-2018-012 5110 ICP-OES' % now,
                         'Z:\\Data\\%s\\66-01-2018-012 5110 ICP-OES' % now,
                         'Z:\\Data\\%s\\66-01-2018-012 5110 ICP-OES' % now,
                         'Z:\\Data\\%s\\66-01-2018-012 5110 ICP-OES' % now,
                         'Z:\\Data\\%s\\Subcon\\厦门质检院\\RawData' % now, 'Z:\\Data\\%s\\Subcon\\厦门质检院\\ZJY-Resuls' % now,
                         'Z:\\QC Chart\\%s' % now,
                         'QC_Chart_Heavy_Metal_66_01_2018_012.xlsx', 'Z:\\Inorganic_batch\\Microwave\\Result\\Reach',
                         'SVHC_DCU.xlsx', 'Z:\\Inorganic_batch\\Microwave\\Result\\Reach',
                         'Z:\\Inorganic\\Program\\1.Inorganic Operate\\1.New edition\\2.Model',
                         'REACH_SVHC_Candidate_List.csv', '"||||||"六根，少了或者多了都无法读取配置文件',
                         'Z:\\Inorganic_batch\\Formaldehyde\\Batch', 'Z:\\Inorganic_batch\\Formaldehyde\\Batch',
                         'Z:\\Inorganic_batch\\Formaldehyde\\Result',
                         '默认，可更改为自己需要的', 'Z:\\QC Chart\\%s' % now, 'QC_Chart_HCHO_66_01_2016_051_CARY60.xlsx',
                         'QC_Chart_Cr_66_01_2013_011_CARY100.xlsx', 'QC_Chart _pH_66_01_2014_015.xlsx',
                         'QC_Chart _pH_66_01_2018_006.xlsx', 'Z:\\Data\\%s\\66-01-2016-051 UV-Vis (60)\\Formal' % now,
                         'Z:\\Data\\%s\\66-01-2013-011 UV-Vis (100)\\Cr-VI\\Data' % now,
                         'Z:\\Data\\%s\\66-01-2014-015 pH' % now,
                         'Z:\\Data\\%s\\66-01-2018-006 pH' % now]
        f1 = open('%s/config.txt' % configFileUrl, "w", encoding="utf-8")
        i = 0
        for i in range(len(configContentName)):
            f1.write(configContentName[i] + '||||||' + configContent[i] + '\n')
            i += 1
        self.lineEdit_6.setText("配置文件创建成功")
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

    def getBatch(self, messages):
        # 获取Sample ID 、实验方法、质量、体积
        # address = os.path.abspath('.')
        self.lineEdit_6.clear()
        global labNumber
        global qualityValue
        global volumeValue
        global analyteList
        global batchNum
        global selectBatchFile
        labNumber = []
        qualityValue = []
        volumeValue = []
        analyteList = []
        batchNum = []
        if messages == 'ICP':
            self.textBrowser_3.clear()
            selectBatchFile = QFileDialog.getOpenFileNames(self, '选择Batch文件',
                                                           '%s' % configContent['ICP_Batch_Import_URL'],
                                                           'Wrod files(*.doc*)')
        elif messages == 'UV':
            self.textBrowser_4.clear()
            selectBatchFile = QFileDialog.getOpenFileNames(self, '选择Batch文件',
                                                           '%s' % configContent['UV_Batch_Import_URL'],
                                                           'Wrod files(*.doc*)')
        else:
            selectBatchFile = QFileDialog.getOpenFileNames(self, '选择Batch文件',
                                                           '%s' % configContent['ICP_Batch_Import_URL'],
                                                           'Wrod files(*.doc*)')
        # print(selectBatchFile)
        if selectBatchFile[0] != []:
            self.lineEdit_6.setText("正在抓取样品单号")
            if messages == 'ICP':
                self.textBrowser_3.append("正在抓取样品单号")
                self.textBrowser_3.append("样品单号抓取完成后，\n才可以开始下一步骤！！！")
            elif messages == 'UV':
                self.textBrowser_4.append("正在抓取样品单号")
                self.textBrowser_4.append("样品单号抓取完成后，\n才可以开始下一步骤！！！")
            if messages == 'Auto':
                self.lineEdit.clear()
                self.lineEdit.setText('Sample ID')
            app.processEvents()
            w = Dispatch('Word.Application')
            w.Visible = 0
            n = 0
            for n in range(len(selectBatchFile[0])):
                fileName = os.path.split(selectBatchFile[0][n])[1]
                if messages == 'ICP':
                    self.textBrowser_3.append('%s：%s' % (n + 1, fileName))
                if messages == 'UV':
                    self.textBrowser_4.append('%s：%s' % (n + 1, fileName))
                app.processEvents()
                # win系统识别路径为“\”
                doc = w.Documents.Open(r"%s" % selectBatchFile[0][n].replace('/', '\\'))
                a = doc.Content.Text
                b = a.split('\r')
                # print(b)
                doc.Close()
                i = 0
                for i in range(len(b)):
                    if ('/' in b[i]) and (len(b[i]) > 5) and ('/' + str(last_time) not in b[i]) and (
                            '/' + str(now) not in b[i]) and ('GB/T' not in b[i]) and ('D' not in b[i]):
                        labNumber.append(b[i])
                        qualityValue.append(b[i + 4])
                        volumeValue.append(b[i + 2])
                        analyteList.append(b[i + 5])
                        batchNum.append(b[4])
                        app.processEvents()
                n += 1
            self.lineEdit_6.setText("样品单号抓取完成")
            if messages == 'ICP':
                self.textBrowser_3.append("样品单号抓取完成")
            elif messages == 'UV':
                self.textBrowser_4.append("样品单号抓取完成")
            w.Quit()
            app.processEvents()
            # print(labNumber, qualityValue, volumeValue)
            # print(batchNum)
        else:
            self.lineEdit_6.setText("请重新选择Batch文件")

    def icpBatch(self):
        # ICP仪器使用
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'ICP')
                if labNumber == []:
                    self.textBrowser_3.append("请重新选择Batch数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_3.append("请重新选择Batch数据文件")
                m = 'N'
        if m == 'Y':
            self.textBrowser_3.append("正在微波ICP Batch转化")
            app.processEvents()
            f1 = open('%s/ICP %s.txt' % (desktopUrl, today), "a+", encoding="utf-8")
            f1.write('\n')
            i = 0
            for i in range(len(labNumber)):
                # print(analyteList[i],qualityValue[i])
                if i<len(labNumber)-1:
                    if batchNum[i] != batchNum[i-1]:
                        f1.write('\n')
                if ('1811' in analyteList[i]) or ('1811' in qualityValue[i]):
                    f1.write('%sA' % labNumber[i] + '\n')
                    f1.write('%sB' % labNumber[i] + '\n')
                    f1.write('%sC' % labNumber[i] + '\n')
                    i += 1
                else:
                    f1.write(labNumber[i] + '\n')
                    i += 1
            self.textBrowser_3.append("完成微波ICP Batch转化")
            self.textBrowser_3.append("生成路径：%s" % desktopUrl)
            self.lineEdit_6.setText("ICP Sample ID转化完成")

    def aasBatch(self):
        # AAS仪器使用
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'

        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'ICP')
                if labNumber == []:
                    self.textBrowser_3.append("请重新选择Batch数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_3.append("请重新选择Batch数据文件")
                m = 'N'
        if m =='Y':
                self.textBrowser_3.append("正在微波Batch-AAS转化")
                app.processEvents()
                f1 = open('%s/AAS %s.txt' % (desktopUrl, today), "a+", encoding="utf-8")
                f1.write('\n')
                i = 0
                for i in range(len(labNumber)):
                    if i < len(labNumber) - 1:
                        if batchNum[i] != batchNum[i - 1]:
                            f1.write('\n')
                    f1.write(labNumber[i].replace('+', '-') + '\n')
                    i += 1
                self.textBrowser_3.append("完成微波Batch-AAS转化")
                self.textBrowser_3.append("生成路径：%s" % desktopUrl)
                self.lineEdit_6.setText("AAS Sample ID转化完成")

    def nickelBatch(self):
        # 镍释放模板
        # 判断是否有选择Batch文件
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'

        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'ICP')
                if labNumber == []:
                    self.textBrowser_3.append("请重新选择Batch数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_3.append("请重新选择Batch数据文件")
                m = 'N'
        if m == 'Y':
            # 判断是否有镍释放的模板文件
            file = configContent['Nickel_Batch_Import_URL'] + '\\' + configContent['Nickel_File_Name']
            folder1 = os.path.exists(file)
            if not folder1:
                QMessageBox.information(self, "无镍释放模板",
                                        "没有Nickel结果模板文件！！！\n请查看config配置文件内容是否符合需求。\nNickel_Batch_Import_URL,Nickel_File_Name\n镍释放结果模板的文件路径、文件名称和Excel格式",
                                        QMessageBox.Yes)
            # 判断镍释放存储路径是否存在
            fileUrl = configContent['Nickel_Batch_Export_URL']
            folder2 = os.path.exists(fileUrl)
            if not folder2:
                QMessageBox.information(self, "镍释放路径错误",
                                        "没有镍释放存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nNickel_Batch_Export_URL",
                                        QMessageBox.Yes)
            if (not folder1) or (not folder2):
                self.textBrowser_3.append("请更改配置文件并导入后，重新点击Nickel Batch按钮开始数据处理")
            else:
                if ('1811' in analyteList[0]) or ('1811' in qualityValue[0]):
                    self.textBrowser_3.append("正在镍释放Batch转化")
                    self.lineEdit_6.setText("正在镍释放Batch转化")
                    app.processEvents()
                    excel = win32com.gencache.EnsureDispatch('Excel.Application')
                    excel.Visible = 0
                    excel.Application.DisplayAlerts = False  # False为另存为自动保存，True为弹出提示保存
                    wb = excel.Workbooks.Open(
                        os.path.join(os.getcwd(), r'%s/%s' % (
                            configContent['Nickel_Batch_Import_URL'], configContent['Nickel_File_Name'])))
                    ws = wb.Worksheets('Data')
                    x = 1
                    oneRow = []
                    while ws.Cells(1, x).Value is not None:
                        oneRow.append(ws.Cells(1, x).Value)
                        x += 1
                    sampleColumn = int(oneRow.index('Sample ID')) + 1
                    noColumn = int(oneRow.index('No.')) + 1
                    n = 2
                    num = []
                    while ws.Cells(n, noColumn).Value is not None:
                        num.append(ws.Cells(n, noColumn).Value)
                        n += 1
                    i = 0
                    m = 1
                    n = 2
                    for each in labNumber:
                        if i < len(labNumber):
                            if (i + 1) % num[-1] != 0:
                                ws.Cells(n, sampleColumn).Value = each
                                n += 1
                                i += 1
                            else:
                                ws.Cells(n, sampleColumn).Value = each
                                wb.SaveAs('%s/Ni %s-%s.xlsm' % (configContent['Nickel_Batch_Export_URL'], today, m))
                                n = 2
                                i += 1
                                m += 1
                                wb = excel.Workbooks.Open(
                                    os.path.join(os.getcwd(), r'%s/%s' % (
                                        configContent['Nickel_Batch_Import_URL'], configContent['Nickel_File_Name'])))
                                ws = wb.Worksheets('Data')
                    if (i + 1) % num[-1] != 1:
                        wb.SaveAs('%s/Ni %s-%s.xlsm' % (configContent['Nickel_Batch_Export_URL'], today, m))
                    excel.Quit()
                    self.textBrowser_3.append("完成镍释放Batch转化")
                    self.textBrowser_3.append("生成路径：%s" % configContent['Nickel_Batch_Export_URL'])
                    self.lineEdit_6.setText("完成镍释放Batch转化")
                else:
                    self.textBrowser_3.append("请确认Batch方法是镍释放")
                    self.lineEdit_6.setText("请确认Batch方法是镍释放")

    def ecoZjy(self):
        # ECO质检院模板生成
        # 判断是否选择了Batch文件
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'

        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'ICP')
                if labNumber == []:
                    self.textBrowser_3.append("请重新选择Batch数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_3.append("请重新选择Batch数据文件")
                m = 'N'
        if m == 'Y':
            # 判断ECO存储路径是否存在
            fileUrl = configContent['ECO_Batch_Export_URL']
            folder = os.path.exists(fileUrl)
            if not folder:
                QMessageBox.information(self, "ECO存储路劲出错",
                                        "没有ECO存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nECO_Batch_Export_URL",
                                        QMessageBox.Yes)
                self.textBrowser_3.append("请更改配置文件并导入后，重新点击ECO ZJY按钮开始数据处理")
            else:
                self.textBrowser_3.append("正在ECO质检院Batch转化")
                self.lineEdit_6.setText("正在ECO质检院Batch转化")
                app.processEvents()
                ecoFile = os.path.exists('%s/ECO ZJY %s.xlsx' % (configContent['ECO_Batch_Export_URL'], today))
                excel = win32com.gencache.EnsureDispatch('Excel.Application')
                excel.Visible = 0
                if not ecoFile:
                    wb = excel.Workbooks.Add()
                    ws = wb.Worksheets('Sheet1')
                    ws.Columns(1).ColumnWidth = 3  # 列宽。
                    ws.Columns(2).ColumnWidth = 12.5  # 列宽。
                    ws.Columns(3).ColumnWidth = 14.5  # 列宽。
                    ws.Columns(4).ColumnWidth = 6.5  # 列宽。
                    ws.Columns(5).ColumnWidth = 6.6  # 列宽。
                    ws.Columns(6).ColumnWidth = 6  # 列宽。
                    ws.Columns(7).ColumnWidth = 20  # 列宽。
                    ws.Cells(1, 1).Value = 'No.'
                    ws.Cells(1, 2).Value = 'Sample No.'
                    ws.Cells(1, 3).Value = 'Analyte'
                    ws.Cells(1, 4).Value = 'Weight'
                    ws.Cells(1, 5).Value = 'Volume'
                    ws.Cells(1, 6).Value = 'DF'
                    ws.Cells(1, 7).Value = 'Batch No'
                    ws.Cells(2, 1).Value = 1
                    ws.Cells(2, 2).Value = 'BLK'
                    ws.Cells(2, 6).Value = 5
                    m = 0
                    for m in range(2):
                        x = 0
                        for x in range(7):
                            ws.Cells(m + 1, x + 1).BorderAround(1, 2)  # 表格边框
                            ws.Cells(m + 1, x + 1).HorizontalAlignment = -4108
                            x += 1
                        m += 1
                    i = 0
                    n = 3
                    for i in range(len(labNumber)):
                        ws.Cells(n, 1).Value = '%s' % (n - 1)
                        ws.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws.Cells(n, 3).Value = '%s' % analyteList[i]
                        ws.Cells(n, 4).Value = '%s' % qualityValue[i]
                        ws.Cells(n, 5).Value = '%s' % volumeValue[i]
                        ws.Cells(n, 6).Value = 5
                        ws.Cells(n, 7).Value = '%s' % batchNum[i].replace('\x1e', '-')
                        x = 0
                        for x in range(7):
                            ws.Cells(n, x + 1).BorderAround(1, 2)
                            ws.Cells(n, x + 1).HorizontalAlignment = -4108
                            x += 1
                        n += 1
                        i += 1
                    wb.Worksheets.Add()
                    ws2 = excel.Worksheets('Sheet2')
                    ws2.Cells(1, 1).Value = '1.'
                    ws2.Cells(1, 1).HorizontalAlignment = -4108  # 居中
                    ws2.Cells(1, 1).Font.Size = 12
                    ws2.Cells(1, 1).Font.Bold = True
                    ws2.Cells(1, 2).Value = 'BLK'
                    ws2.Cells(1, 2).HorizontalAlignment = -4108
                    ws2.Cells(1, 2).Font.Size = 12
                    ws2.Cells(1, 2).Font.Bold = True
                    ws2.Rows(1).RowHeight = 33.8  # 行高
                    ws2.Columns(1).ColumnWidth = 2.8  # 列宽。
                    ws2.Columns(2).ColumnWidth = 15.2  # 列宽。
                    i = 0
                    n = 2
                    for i in range(len(labNumber)):
                        ws2.Rows(n).RowHeight = 33.8  # 行高
                        ws2.Cells(n, 1).Value = '%s.' % n
                        ws2.Cells(n, 1).HorizontalAlignment = -4108
                        ws2.Cells(n, 1).Font.Size = 12
                        ws2.Cells(n, 1).Font.Bold = True
                        ws2.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws2.Cells(n, 2).HorizontalAlignment = -4108
                        ws2.Cells(n, 2).Font.Size = 12
                        ws2.Cells(n, 2).Font.Bold = True
                        n += 1
                        i += 1
                else:
                    excel.Application.DisplayAlerts = False  # False为另存为自动保存，True为弹出提示保存
                    wb = excel.Workbooks.Open(
                        os.path.join(os.getcwd(),
                                     r'%s/ECO ZJY %s.xlsx' % (configContent['ECO_Batch_Export_URL'], today)))
                    ws = wb.Worksheets('Sheet1')
                    i = 0
                    n = 1
                    while ws.Cells(n, 1).Value is not None:
                        n += 1
                    for i in range(len(labNumber)):
                        ws.Cells(n, 1).Value = '%s' % (n - 1)
                        ws.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws.Cells(n, 3).Value = '%s' % analyteList[i]
                        ws.Cells(n, 4).Value = '%s' % qualityValue[i]
                        ws.Cells(n, 5).Value = '%s' % volumeValue[i]
                        ws.Cells(n, 5).NumberFormat = "0"
                        ws.Cells(n, 6).Value = 5
                        ws.Cells(n, 7).Value = '%s' % batchNum[i].replace('\x1e', '-')
                        x = 0
                        for x in range(7):
                            ws.Cells(n, x + 1).BorderAround(1, 2)
                            ws.Cells(n, x + 1).HorizontalAlignment = -4108
                            x += 1
                        n += 1
                        i += 1
                    ws2 = excel.Worksheets('Sheet2')
                    i = 0
                    n = 1
                    while ws2.Cells(n, 1).Value is not None:
                        n += 1
                    for i in range(len(labNumber)):
                        ws2.Rows(n).RowHeight = 33.8  # 行高
                        ws2.Cells(n, 1).Value = '%s.' % n
                        ws2.Cells(n, 1).HorizontalAlignment = -4108
                        ws2.Cells(n, 1).Font.Size = 12
                        ws2.Cells(n, 1).Font.Bold = True
                        ws2.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws2.Cells(n, 2).HorizontalAlignment = -4108
                        ws2.Cells(n, 2).Font.Size = 12
                        ws2.Cells(n, 2).Font.Bold = True
                        n += 1
                        i += 1
                list1 = ['Analyte', 'Sb', 'As', 'Cd', 'Cr', 'Co', 'Cu', 'Pb', 'Hg', 'Ni', 'Ba', 'Se']
                list2 = ['MDL(ug/L)', 2, 0.8, 0.4, 2, 2, 2, 0.8, 0.08, 2, 2, 2]
                list3 = ['Limit(mg/kg)', '<5', '<0.2', '<0.1', '<1', '<1', '<25', '0.8', '<0.02', '<1', '<1000', '<500']
                i = 0
                n += 1
                for i in range(len(list1)):
                    ws.Cells(n, 2).Value = '%s' % list1[i]
                    ws.Cells(n, 3).Value = '%s' % list2[i]
                    ws.Cells(n, 4).Value = '%s' % list3[i]
                    x = 1
                    for m in range(3):
                        ws.Cells(n, x + 1).BorderAround(1, 2)
                        ws.Cells(n, x + 1).HorizontalAlignment = -4108
                        x += 1
                    i += 1
                    n += 1
                wb.SaveAs('%s/ECO ZJY %s.xlsx' % (configContent['ECO_Batch_Export_URL'], today))
                excel.Quit()
                self.textBrowser_3.append("ECO质检院Batch转化完成")
                self.textBrowser_3.append("生成路径：%s" % configContent['ECO_Batch_Export_URL'])
                self.lineEdit_6.setText("ECO质检院Batch转化完成")
                app.processEvents()

    def ecoZxd(self):
        # ECO中迅德模板生成
        # 判断是否选择了Batch文件
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'ICP')
                if labNumber == []:
                    self.textBrowser_3.append("请重新选择Batch数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_3.append("请重新选择Batch数据文件")
        if m == 'Y':
            # 判断ECO存储路径是否存在
            fileUrl = configContent['ECO_Batch_Export_URL']
            folder = os.path.exists(fileUrl)
            if not folder:
                QMessageBox.information(self, "ECO存储路劲出错",
                                        "没有ECO存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nECO_Batch_Export_URL",
                                        QMessageBox.Yes)
                self.textBrowser_3.append("请更改配置文件并导入后，重新点击ECO ZXD按钮开始数据处理")
            else:
                self.textBrowser_3.append("正在ECO中迅德Batch转化")
                self.lineEdit_6.setText("正在ECO中迅德Batch转化")
                app.processEvents()
                ecoFile = os.path.exists('%s/ECO ZXD %s.xlsx' % (configContent['ECO_Batch_Export_URL'], today))
                excel = win32com.gencache.EnsureDispatch('Excel.Application')
                excel.Visible = 0
                if not ecoFile:
                    wb = excel.Workbooks.Add()
                    ws = wb.Worksheets('Sheet1')
                    # 创建Batch单号
                    ws.Columns(1).ColumnWidth = 3  # 列宽。
                    ws.Columns(2).ColumnWidth = 12.5  # 列宽。
                    ws.Columns(3).ColumnWidth = 14.5  # 列宽。
                    ws.Columns(4).ColumnWidth = 6.5  # 列宽。
                    ws.Columns(5).ColumnWidth = 6.6  # 列宽。
                    ws.Columns(6).ColumnWidth = 6  # 列宽。
                    ws.Columns(7).ColumnWidth = 20  # 列宽。
                    ws.Cells(1, 1).Value = 'No.'
                    ws.Cells(1, 2).Value = 'Sample No.'
                    ws.Cells(1, 3).Value = 'Analyte'
                    ws.Cells(1, 4).Value = 'Weight'
                    ws.Cells(1, 5).Value = 'Volume'
                    ws.Cells(1, 6).Value = 'DF'
                    ws.Cells(1, 7).Value = 'Batch No'
                    ws.Cells(2, 1).Value = 1
                    ws.Cells(2, 2).Value = 'BLK'
                    ws.Cells(2, 6).Value = 5
                    m = 0
                    for m in range(2):
                        x = 0
                        for x in range(7):
                            ws.Cells(m + 1, x + 1).BorderAround(1, 2)  # 表格边框
                            ws.Cells(m + 1, x + 1).HorizontalAlignment = -4108
                            x += 1
                        m += 1
                    i = 0
                    n = 3
                    for i in range(len(labNumber)):
                        ws.Cells(n, 1).Value = '%s' % (n - 1)
                        ws.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws.Cells(n, 3).Value = '%s' % analyteList[i]
                        ws.Cells(n, 4).Value = '%s' % qualityValue[i]
                        ws.Cells(n, 5).Value = '%s' % volumeValue[i]
                        ws.Cells(n, 6).Value = 5
                        ws.Cells(n, 7).Value = '%s' % batchNum[i].replace('\x1e', '-')
                        x = 0
                        for x in range(7):
                            ws.Cells(n, x + 1).BorderAround(1, 2)
                            ws.Cells(n, x + 1).HorizontalAlignment = -4108
                            x += 1
                        n += 1
                        i += 1
                    # 创建打印标签
                    wb.Worksheets.Add()
                    ws2 = excel.Worksheets('Sheet2')
                    ws2.Cells(1, 1).Value = '1.'
                    ws2.Cells(1, 1).HorizontalAlignment = -4108  # 居中
                    ws2.Cells(1, 1).Font.Size = 12
                    ws2.Cells(1, 1).Font.Bold = True
                    ws2.Cells(1, 2).Value = 'BLK'
                    ws2.Cells(1, 2).HorizontalAlignment = -4108
                    ws2.Cells(1, 2).Font.Size = 12
                    ws2.Cells(1, 2).Font.Bold = True
                    ws2.Rows(1).RowHeight = 33.8  # 行高
                    ws2.Columns(1).ColumnWidth = 2.8  # 列宽。
                    ws2.Columns(2).ColumnWidth = 15.2  # 列宽。
                    i = 0
                    n = 2
                    for i in range(len(labNumber)):
                        ws2.Rows(n).RowHeight = 33.8  # 行高
                        ws2.Cells(n, 1).Value = '%s.' % n
                        ws2.Cells(n, 1).HorizontalAlignment = -4108
                        ws2.Cells(n, 1).Font.Size = 12
                        ws2.Cells(n, 1).Font.Bold = True
                        ws2.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws2.Cells(n, 2).HorizontalAlignment = -4108
                        ws2.Cells(n, 2).Font.Size = 12
                        ws2.Cells(n, 2).Font.Bold = True
                        n += 1
                        i += 1
                else:
                    excel.Application.DisplayAlerts = False
                    wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s/ECO ZXD %s.xlsx' % (
                        configContent['ECO_Batch_Export_URL'], today)))
                    ws = wb.Worksheets('Sheet1')
                    i = 0
                    n = 1
                    while ws.Cells(n, 1).Value is not None:
                        n += 1
                    for i in range(len(labNumber)):
                        ws.Cells(n, 1).Value = '%s' % (n - 1)
                        ws.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws.Cells(n, 3).Value = '%s' % analyteList[i]
                        ws.Cells(n, 4).Value = '%s' % qualityValue[i]
                        ws.Cells(n, 5).Value = '%s' % volumeValue[i]
                        ws.Cells(n, 5).NumberFormat = "0"
                        ws.Cells(n, 6).Value = 5
                        ws.Cells(n, 7).Value = '%s' % batchNum[i].replace('\x1e', '-')
                        x = 0
                        for x in range(7):
                            ws.Cells(n, x + 1).BorderAround(1, 2)
                            ws.Cells(n, x + 1).HorizontalAlignment = -4108
                            x += 1
                        n += 1
                        i += 1
                    ws2 = excel.Worksheets('Sheet2')
                    i = 0
                    n = 1
                    while ws2.Cells(n, 1).Value is not None:
                        n += 1
                    for i in range(len(labNumber)):
                        ws2.Rows(n).RowHeight = 33.8  # 行高
                        ws2.Cells(n, 1).Value = '%s.' % n
                        ws2.Cells(n, 1).HorizontalAlignment = -4108
                        ws2.Cells(n, 1).Font.Size = 12
                        ws2.Cells(n, 1).Font.Bold = True
                        ws2.Cells(n, 2).Value = '%s' % labNumber[i]
                        ws2.Cells(n, 2).HorizontalAlignment = -4108
                        ws2.Cells(n, 2).Font.Size = 12
                        ws2.Cells(n, 2).Font.Bold = True
                        n += 1
                        i += 1
                list1 = ['Analyte', 'Sb', 'As', 'Cd', 'Cr', 'Co', 'Cu', 'Pb', 'Hg', 'Ni', 'Ba', 'Se', 'Mn', 'Zn', 'Al',
                         'Ti', 'Zr']
                list2 = ['RL', 0.5, 0.2, 0.1, 0.5, 0.5, 0.5, 0.2, 0.02, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
                list3 = ['DL', 2, 2, 0.2, 2, 2, 2, 2, 0.2, 2, 2, 2, 2, 2, 2, 2, 2]
                i = 0
                n += 1
                for i in range(len(list1)):
                    ws.Cells(n, 2).Value = '%s' % list1[i]
                    ws.Cells(n, 3).Value = '%s' % list2[i]
                    ws.Cells(n, 4).Value = '%s' % list3[i]
                    if i == 0:
                        ws.Cells(n, 5).Value = 'UV'
                        ws.Cells(n, 6).Value = 'Unit'
                        ws.Cells(n, 7).Value = 'Unit (Raw Data)'
                    else:
                        ws.Cells(n, 5).Value = '10%'
                        ws.Cells(n, 6).Value = 'mg/kg'
                        ws.Cells(n, 7).Value = 'ug/L'
                    x = 1
                    for m in range(6):
                        ws.Cells(n, x + 1).BorderAround(1, 2)
                        ws.Cells(n, x + 1).HorizontalAlignment = -4108
                        x += 1
                    i += 1
                    n += 1
                wb.SaveAs('%s/ECO ZXD %s.xlsx' % (configContent['ECO_Batch_Export_URL'], today))
                excel.Quit()
                self.textBrowser_3.append("ECO中迅德Batch转化完成")
                self.textBrowser_3.append("生成路径：%s" % configContent['ECO_Batch_Export_URL'])
                self.lineEdit_6.setText("ECO中迅德Batch转化完成")
                app.processEvents()

    def formalBatch(self):
        # 获取甲醛Batch信息
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'
        if m =='N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'UV')
                if labNumber == []:
                    self.textBrowser_4.append("请重新选择Batch数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_4.append("请重新选择Batch数据文件")
        if m == 'Y':
            # 判断存储路径是否存在
            fileUrl = configContent['UV_Batch_Export_URL']
            folder = os.path.exists(fileUrl)
            if not folder:
                QMessageBox.information(self, "ICP结果路径出错",
                                        "没有ICP结果转化为TXT的存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nUV_Batch_Export_URL",
                                        QMessageBox.Yes)
                self.textBrowser.append("重新更改配置文件并导入后，重新点击Formal Batch按钮开始数据处理")
            else:
                self.textBrowser_4.append("样品单号正在生成Formal格式")
                self.lineEdit_6.setText("样品单号正在生成Formal格式")
                app.processEvents()
                n = 3
                jNum = []
                lNum = []
                fNum = []
                # 获取日本方法和其它方法的单号位置
                for i in range(len(labNumber)):
                    # print(labNumber[i],analyteList[i])
                    if '1041' in analyteList[i]:
                        jNum.append(i)
                    elif '17226' in analyteList[i]:
                        lNum.append(i)
                    else:
                        fNum.append(i)
                if jNum !=[]:
                    file = open('%s/Formal JISL %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                    for i in jNum:
                            file.write('A0-%s\n' % labNumber[i])
                    for i in jNum:
                        if 'A' in analyteList[i]:
                            file.write('A1-%s\n' % labNumber[i])
                        else:
                            file.write('A2-%s\n' % labNumber[i])
                    file.write('As-4.5\n')
                    file.write('QC\n')
                if lNum != []:
                    fileName = '%s/Formal 17226 %s.txt' % (configContent['UV_Batch_Export_URL'], today)
                    for i in lNum:
                        if not os.path.exists(fileName):
                            file = open('%s/Formal 17226 %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                            file.write('BLK\n')
                            file.write('BS\n')
                            file.write('SS\n')
                            file.write('%s\n' % labNumber[i])
                            n += 1
                        else:
                            file = open('%s/Formal 17226 %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                            file.write('%s\n' % labNumber[i])
                            n += 1
                            if n % 20 == 0:
                                file.write('QC\n')
                    if n % 20 != 0:
                        file.write('QC\n')
                    for i in lNum:
                        file = open('%s/Formal 17226 %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                        file.write('%sB\n' % labNumber[i])
                        n += 1
                    file.write('QC\n')
                if fNum !=[]:
                    fileName = '%s/Formal 14184 %s.txt' % (configContent['UV_Batch_Export_URL'],today)
                    for i in fNum:
                        if not os.path.exists(fileName):
                            file = open('%s/Formal 14184 %s.txt' % (configContent['UV_Batch_Export_URL'],today), 'a+')
                            file.write('BLK\n')
                            file.write('BS\n')
                            file.write('SS\n')
                            file.write('%s\n' % labNumber[i])
                            n += 1
                        else:
                            file = open('%s/Formal 14184 %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                            file.write('%s\n'%labNumber[i])
                            n += 1
                            if n % 20 == 0:
                                file.write('QC\n')
                    if n % 20 != 0:
                        file.write('QC\n')
                self.textBrowser_4.append("完成样品单号Formal-Batch")
                self.textBrowser_4.append("生成路径：%s"% configContent['UV_Batch_Export_URL'])
                self.lineEdit_6.setText("完成样品单号Formal-Batch")

    def crBatch(self):
        # 获取六价铬Batch信息
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'UV')
                if labNumber == []:
                    self.textBrowser_4.append("请重新选择Batch数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_4.append("请重新选择Batch数据文件")
        if m == 'Y':
            # 判断存储路径是否存在
            fileUrl = configContent['UV_Batch_Export_URL']
            folder = os.path.exists(fileUrl)
            if not folder:
                QMessageBox.information(self, "ICP结果路径出错",
                                        "没有ICP结果转化为TXT的存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nUV_Batch_Export_URL",
                                        QMessageBox.Yes)
                self.textBrowser.append("重新更改配置文件并导入后，重新点击Cr VI Batch按钮开始数据处理")
            else:
                self.textBrowser_4.append("样品单号正在生成Cr VI格式")
                self.lineEdit_6.setText("样品单号正在生成Cr VI格式")
                app.processEvents()
                n = 1
                fileName = '%s/Cr VI %s.txt' % (configContent['UV_Batch_Export_URL'], today)
                if not os.path.exists(fileName):
                    file = open('%s/Cr VI %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                    file.write('BLK\n')
                    file.write('BLK+DPC\n')
                    file.write('BS\n')
                    file.write('BS+DPC\n')
                    n = 2
                for each in labNumber:
                    file = open('%s/Cr VI %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                    file.write('%s\n' % each)
                    file.write('%s+D\n' % each)
                    n += 1
                    if n % 20 == 0:
                        file.write('QC\n')
                if n % 20 != 0:
                    file.write('QC\n')
                for each in labNumber:
                    file = open('%s/Cr VI %s.txt' % (configContent['UV_Batch_Export_URL'], today), 'a+')
                    file.write('%s+S\n' % each)
                file.write('QC\n')
            self.textBrowser_4.append("完成样品单号Cr VI-Batch")
            self.textBrowser_4.append("生成路径：%s" % configContent['UV_Batch_Export_URL'])
            self.lineEdit_6.setText("完成样品单号Cr VI-Batch")

    def phBatch(self):
        # 获取pH-Batch信息
        try:
            labNumber
        except NameError:
            m = 'N'
        else:
            if labNumber == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'UV')
                if labNumber == []:
                    self.textBrowser_4.append("请重新选择Batch数据文件")
                    app.processEvents()
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_4.append("请重新选择Batch数据文件")
                app.processEvents()
        if m == 'Y':
            # 判断存储路径是否存在
            fileUrl = configContent['UV_Batch_Export_URL']
            folder = os.path.exists(fileUrl)
            fileUrl2 = configContent['UV_Rusult_Export_URL']
            folder2 = os.path.exists(fileUrl2)
            if (not folder) or (not folder2):
                QMessageBox.information(self, "ICP结果路径出错",
                                        "没有ICP结果转化为TXT的存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nUV_Batch_Export_URL,UV_Rusult_Export_URL",
                                        QMessageBox.Yes)
                self.textBrowser.append("重新更改配置文件并导入后，重新点击pH Batch按钮开始数据处理")
            else:
                self.textBrowser_4.append("样品单号正在生成新旧pH格式")
                self.lineEdit_6.setText("样品单号正在生成新旧pH格式")
                app.processEvents()
                # 判断存储文件是否存在
                nowTime = time.strftime('%Y-%m-%d %H:%M:%S ')
                lNum = []
                fNum = []
                batchNum = []
                batchLab = []
                resultNum = []
                resultLab= []
                for i in range(len(labNumber)):
                    if '4045' in analyteList[i]:
                        lNum.append(i)
                    else:
                        fNum.append(i)
                fileBatch = configContent['UV_Batch_Export_URL']+'/'+'pH Batch %s.csv'%today
                folder3 = os.path.exists(fileBatch)
                fileResult = configContent['UV_Rusult_Export_URL']+'/'+'pH Result %s.csv'%today
                folder4 = os.path.exists(fileResult)
                if lNum != [] or fNum !=[]:
                    if not folder3:
                        # Batch模板
                        batchOne = ['pH cal','pH Measure','pH Measure','pH Measure']
                        batchThree = ['Standard','CC','BLK','BLK']
                        batchFour = ['','QC','Before','After']
                        batchData = pd.DataFrame({'a': batchOne, 'b': 1, 'c': batchThree,'d':batchFour,'e':'','f':'','g':'','h':'','i':'','j':'','k':'1'})
                        batchData.to_csv(fileBatch, mode='a', index=0, header=0)
                        # Result模板
                        resultOne = ['Determination start','','%s UTC+8'%nowTime,'%s UTC+8'%nowTime,'%s UTC+8'%nowTime,'%s UTC+8'%nowTime,]
                        resultTwo = ['Method name','','pH Cal','pH Measure','pH Measure','pH Measure']
                        resultThree = ['ID1.Value','','Standard','CC','BLK','BLK']
                        resultFour = ['ID2.Value','','','QC','before','after',]
                        resultFive = ['RS01.Name','','','pH','pH','pH']
                        resultSix = ['RS01.Value','','','','','']
                        resultSeven = ['RS02.Name','','','T','T','T']
                        resultEight = ['RS02.Value','','','','','']
                        resultNine = ['Lab TEMP','','','','','']
                        resultTen = ['[DELTA]ph','','0','','','']
                        resultData = pd.DataFrame(
                            {'a': resultOne, 'b': resultTwo, 'c': resultThree, 'd': resultFour, 'e':resultFive , 'f': resultSix, 'g': resultSeven, 'h': resultEight,
                             'i': resultNine, 'j': resultTen})
                        resultData.to_csv(fileResult, mode='a', index=0, header=0)
                if fNum != []:
                    num, ok = QInputDialog.getInt(self, '输入3071编号', '输入pH3071第一个样品编号', 1, 1, 999999, 1)
                    if ok and num:
                        n = num
                        for i in fNum:
                            batchNum.append(n)
                            batchNum.append(n)
                            batchNum.append(n)
                            batchLab.append('%s' % labNumber[i])
                            batchLab.append('%sA' % labNumber[i])
                            batchLab.append('%sB' % labNumber[i])
                            if n % 20 == 0:
                                batchNum.append('CC')
                                batchLab.append('QC')
                            n += 1
                        if num == 1:
                            batchNum.append('DI')
                            batchLab.append('Water')
                        if n % 20 != 1:
                            batchNum.append('CC')
                            batchLab.append('QC')
                if lNum != []:
                    num, ok = QInputDialog.getInt(self, '输入4045编号', '输入pH4045第一个样品编号', 1, 1, 999999, 1)
                    if ok and num:
                        l = num
                        if l == 1:
                            batchNum.append('BLK')
                            batchLab.append(4045)
                        for i in lNum:
                            batchNum.append('4045 %s'%l)
                            batchNum.append('4045 %s'%l)
                            batchNum.append('4045 %s'%l)
                            batchNum.append('4045 %s'%l)
                            batchLab.append('%sA' % labNumber[i])
                            batchLab.append('%sB' % labNumber[i])
                            batchLab.append('%sC' % labNumber[i])
                            batchLab.append('%sD' % labNumber[i])
                            if l % 20 == 0:
                                batchNum.append('CC')
                                batchLab.append('QC')
                            l += 1
                        if l % 20 != 1:
                            batchNum.append('CC')
                            batchLab.append('QC')
                if lNum != [] or fNum != []:
                    batchData = pd.DataFrame(
                        {'a': 'pH Measure', 'b': 1, 'c': batchNum, 'd': batchLab, 'e': '', 'f': '', 'g': '', 'h': '',
                         'i': '', 'j': '', 'k': '1'})
                    batchData.to_csv(fileBatch, mode='a', index=0, header=0)
                    resultData = pd.DataFrame(
                        {'a': '%s UTC+8' % nowTime, 'b': 'pH Measure', 'c': batchNum, 'd': batchLab, 'e': 'pH','f':'','g':'T', 'h': ''})
                    resultData.to_csv(fileResult, mode='a', index=0, header=0)
                self.textBrowser_4.append("完成样品单号生成新旧pH格式")
                self.lineEdit_6.setText("完成样品单号生成新旧pH格式")

    def getResult(self, messages):
        # 获取结果文件路径
        global selectResultFile
        self.lineEdit_6.clear()
        self.textBrowser.clear()
        self.textBrowser_5.clear()
        if messages == 'ICP':
            if (self.comboBox.currentText() == 'URL:ICP Result'):
                selectResultFile = QFileDialog.getOpenFileNames(self, '选择ICP-Result文件',
                                                                '%s' % configContent['ICP_Result_Import_URL'],
                                                                'CSV files(*.csv)')
            elif self.comboBox.currentText() == 'URL:ECO ZJY Result':
                selectResultFile = QFileDialog.getOpenFileNames(self, '选择ECO-Result文件',
                                                                '%s' % configContent['ECO_Result_Import_URL'],
                                                                'CSV Files (*.csv;*.txt)')
        elif messages == 'UV':
            if self.comboBox_2.currentText() == 'URL:Formal Result':
                selectResultFile = QFileDialog.getOpenFileNames(self, '选择Formal-Result文件',
                                                                '%s' % configContent['Formal_Result_Import_URL'],
                                                                'CSV files(*.csv)')
            elif self.comboBox_2.currentText() == 'URL:pH 2014 Result':
                selectResultFile = QFileDialog.getOpenFileNames(self, '选择pH2014-Result文件',
                                                                '%s' % configContent['pH2014_Result_Import_URL'],
                                                                'CSV files(*.csv)')
            elif self.comboBox_2.currentText() == 'URL:pH 2018 Result':
                selectResultFile = QFileDialog.getOpenFileNames(self, '选择pH2018-Result文件',
                                                                '%s' % configContent['pH2018_Result_Import_URL'],
                                                                'CSV files(*.csv)')
            elif self.comboBox_2.currentText() == 'URL:Cr VI Result':
                selectResultFile = QFileDialog.getOpenFileNames(self, '选择Cr VI-Result文件',
                                                                '%s' % configContent['Cr_VI_Result_Import_URL'],
                                                                'CSV files(*.csv)')
        # print(1,selectBatchFile[0])
        # 仅获取选择文件的路径
        if selectResultFile[0] != []:
            self.lineEdit_6.setText("正在抓取Result文件")
            if messages == 'ICP':
                self.textBrowser.append("正在抓取Result文件")
            elif   messages == 'UV':
                self.textBrowser_5.append("正在抓取Result文件")
            app.processEvents()
            n = 0
            for n in range(len(selectResultFile[0])):
                fileName = os.path.split(selectResultFile[0][n])[1]
                if messages == 'ICP':
                    self.textBrowser.append('%s：%s' % (n + 1, fileName))
                elif messages == 'UV':
                    self.textBrowser_5.append('%s：%s' % (n + 1, fileName))
                app.processEvents()
            if messages == 'ICP':
                self.textBrowser.append("完成抓取Result文件")
            elif messages == 'UV':
                self.textBrowser_5.append("完成抓取Result文件")
            app.processEvents()
        else:
            self.lineEdit_6.setText("请重新选择Result文件")

    def icpResultToTxt(self):
        # ICP结果转化为TXT
        # 判断是否选择了Result文件
        try:
            selectResultFile[0]
        except NameError:
           m = 'N'
        else:
            if selectResultFile[0] == []:
              m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Result数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getResult(self, 'ICP')
                if selectResultFile[0] == []:
                    self.lineEdit_6.setText("请重新选择ICP Result数据文件")
                    self.textBrowser.append("请重新选择ICP Result数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择ICP Result数据文件")
                self.textBrowser.append("请重新选择ICP Result数据文件")
                m = 'N'
        if m == 'Y':
                # 判断ICP存储路径是否存在
                fileUrl = configContent['ICP_Result_Export_URL']
                folder = os.path.exists(fileUrl)
                if not folder:
                    QMessageBox.information(self, "ICP结果路径出错",
                                            "没有ICP结果转化为TXT的存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nICP_Result_Export_URL",
                                            QMessageBox.Yes)
                    self.textBrowser.append("重新更改配置文件并导入后，重新点击ICP Result按钮开始数据处理")
                else:
                    for fileUrl in selectResultFile[0]:
                        self.textBrowser.append("正在进行ICP文件转换为TXT")
                        self.lineEdit_6.setText("正在进行ICP文件转换为TXT")
                        fileName = os.path.split(fileUrl)[1]
                        app.processEvents()
                        csvFile = pd.read_csv(fileUrl, header=0, names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
                        csvFile = csvFile.drop(['C'], axis=1)
                        csvLine = csvFile.iloc[0]  # 获取行索引为1数据
                        csvLine.replace(['标签', '类型', '元素标签', '浓度', '单位'],
                                        ['Solution Label', 'Type', 'Element', 'Soln Conc', 'Units'], inplace=True)
                        csvFile.to_csv('%s/%s.txt' % (configContent['ICP_Result_Export_URL'], fileName), sep='\t',
                                       index=None, header=None)
                        self.textBrowser.append("完成ICP文件转换为TXT")
                        self.textBrowser.append("生成路径：%s" % configContent['ICP_Result_Export_URL'])
                        self.lineEdit_6.setText("完成ICP文件转换为TXT")

    def reachResult(self):
        # Reach结果转化为TXT
        # 判断是否选择了Batch文件
        try:
            labNumber
        except NameError:
            m3 = 'N'
        else:
            if labNumber == []:
                m3 = 'N'
            else:
                m3 = 'Y'
        if m3 == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Batch数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getBatch(self, 'ICP')
                if labNumber == []:
                    self.textBrowser_3.append("请重新选择Batch数据文件")
                    m3 = 'N'
                else:
                    m3 = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Batch数据文件")
                self.textBrowser_3.append("请重新选择Batch数据文件")
                m3 = 'N'
        # 判断是否选择了Result文件
        try:
            selectResultFile[0]
        except NameError:
            m4 = 'N'
        else:
            if selectResultFile[0] == []:
                m4 = 'N'
            else:
                m4 = 'Y'
        if m4 == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Result数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getResult(self, 'ICP')
                if selectResultFile[0] == []:
                    self.textBrowser.append("请重新选择Result数据文件")
                    self.lineEdit_6.setText("请重新选择Result数据文件")
                    m4 = 'N'
                else:
                    m4 = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择Result数据文件")
                self.textBrowser.append("请重新选择Result数据文件")
                m4 = 'N'
        # 判断是否有Batch和Result文件
        if m3 == 'Y' and m4 == 'Y':
                # 判断是否有Reach模板
                file = configContent['Reach_Result_Import_URL'] + '\\' + configContent['Reach_Result_File_Name']
                folder1 = os.path.exists(file)
                if not folder1:
                    QMessageBox.information(self, "无Reach模板",
                                            "没有Reach结果模板文件！！！\n请查看config配置文件内容是否符合需求。\nReach_Result_Import_URL,Reach_Result_File_Name\nReach结果模板的文件路径、文件名称和Excel格式",
                                            QMessageBox.Yes)
                # 判断Reach存储路径是否存在
                fileUrl = configContent['Reach_Result_Export_URL']
                folder2 = os.path.exists(fileUrl)
                if not folder2:
                    QMessageBox.information(self, "Reach存储路径出错",
                                            "没有Reach结果转化为TXT的存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nReach_Result_Export_URL",
                                            QMessageBox.Yes)
                if (not folder1) or (not folder2):
                    self.textBrowser.append("请更改配置文件并导入后，重新点击Reach Result按钮开始数据处理")
                else:
                    self.textBrowser.append("正在进行Reach结果转换为TXT")
                    self.lineEdit_6.setText("正在进行Reach结果转换为TXT")
                    app.processEvents()
                    excel = win32com.gencache.EnsureDispatch('Excel.Application')
                    excel.Visible = 0
                    excel.Application.DisplayAlerts = True
                    wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s\%s' % (
                        configContent['Reach_Result_Import_URL'], configContent['Reach_Result_File_Name'])))
                    ws = wb.Worksheets('Data')
                    oneRow = []
                    x = 1
                    while ws.Cells(1, x).Value is not None:
                        oneRow.append(ws.Cells(1, x).Value)
                        x += 1
                    sampleColumn = int(oneRow.index('Sample ID')) + 1
                    elementColumn = int(oneRow.index('Element')) + 1
                    concColumn = int(oneRow.index('Sample Conc.')) + 1
                    elements = []
                    resultRows = []
                    n = 2
                    # 获取需要测试元素
                    while ws.Cells(n, elementColumn).Value is not None:
                        elements.append(ws.Cells(n, elementColumn).Value)
                        resultRows.append(n)
                        n += 1
                    # print(elements)
                    # 获取是Reach的Sample ID
                    resultLabnumber = []
                    resultQualityValue = []
                    resultVolumeValue = []
                    i = 0
                    for each in labNumber:
                        # print(labNumber[i], analyteList[i],i)
                        if 'R\x1eI' in analyteList[i]:
                            resultLabnumber.append(each)
                            resultQualityValue.append(qualityValue[i])
                            resultVolumeValue.append(volumeValue[i])
                            # print(resultLabnumber, analyteList[i])
                        i += 1

                    # 获取Sample的结果
                    startNum = int(self.spinBox_3.text())
                    endNum = int(self.spinBox_2.text())
                    if resultLabnumber == []:
                        reply = QMessageBox.question(self, '信息', 'Batch中没有Reach方法，是否需要重新选择Batch数据文件',
                                                     QMessageBox.Yes | QMessageBox.No,
                                                     QMessageBox.Yes)
                        if reply == QMessageBox.Yes:
                            Ui_MainWindow.getBatch(self, 'ICP')
                            self.textBrowser.append("请重新点击Reach Result按钮开始数据处理")
                        else:
                            self.textBrowser.append("确认Batch含有Reach方法")
                            self.lineEdit_6.setText("确认Batch含有Reach方法")
                    else:
                        rusultList = []
                        rusultList2 = []
                        rusultList3 = []
                        rusultList4 = {}
                        for fileUrl in selectResultFile[0]:
                            csvFile = pd.read_csv(fileUrl, header=0, names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
                            csvFile.drop(['B', 'C', 'F', 'G', 'H'], axis=1, inplace=True)
                            csvFile = csvFile[csvFile['A'].isin(resultLabnumber)]
                            csvFile = csvFile[csvFile['D'].isin(elements)]
                            rusultList += list(csvFile['A'])
                            rusultList2 += list(csvFile['D'])
                            rusultList3 += list(csvFile['E'])
                        for num, each in enumerate(rusultList):
                            rusultList4['%s-%s' % (rusultList[num], rusultList2[num])] = rusultList3[num]
                        # 填写excel模板文件
                        if endNum == 0 or endNum > len(resultLabnumber):
                            m = len(resultLabnumber) - startNum + 1
                        else:
                            m = endNum - startNum + 1
                        # print(m)
                        n = startNum - 1
                        # print(rusultList4)
                        # print(elements)
                        for i in range(m):
                            name = resultLabnumber[n].replace("/", '_')
                            self.textBrowser.append("%s:%s" % (n + 1, resultLabnumber[n]))
                            app.processEvents()
                            ws.Cells(2, sampleColumn).Value = resultLabnumber[n]
                            x = 0
                            for e in range(len(elements)):
                                # print(resultLabnumber[n],elements[x])
                                if '%s-%s' % (resultLabnumber[n], elements[x]) in rusultList4.keys():
                                    if str(rusultList4['%s-%s' % (resultLabnumber[n], elements[x])]) == '未校正':
                                        ws.Cells(resultRows[x], concColumn).Value = '未校正'
                                    elif str(rusultList4['%s-%s' % (resultLabnumber[n], elements[x])]) == '####':
                                        ws.Cells(resultRows[x], concColumn).Value = '超出'
                                    else:
                                        ws.Cells(resultRows[x], concColumn).Value = float(
                                            rusultList4['%s-%s' % (resultLabnumber[n], elements[x])]) * int(
                                            resultVolumeValue[n]) / float(resultQualityValue[n])
                                else:
                                    ws.Cells(resultRows[x], concColumn).Value = '未走标准曲线'
                                x += 1
                            # 将excel数据重新填写txt文件中
                            ws1 = wb.Sheets("DCU-Result")
                            resultDcuOne = []
                            resultDcuTwo = []
                            resultDcuThree = []
                            resultDcuFour = []
                            resultDcuFive = []
                            resultDcuSix = []
                            m = 1
                            while ws1.Cells(m, 1).Value is not None:
                                resultDcuOne.append(ws1.Cells(m, 1).Value)
                                resultDcuTwo.append(ws1.Cells(m, 2).Value)
                                resultDcuThree.append(ws1.Cells(m, 3).Value)
                                resultDcuFour.append(ws1.Cells(m, 4).Value)
                                resultDcuFive.append(ws1.Cells(m, 5).Value)
                                resultDcuSix.append(ws1.Cells(m, 6).Value)
                                m += 1
                            folder = os.path.exists(configContent['Reach_Result_Export_URL'] + '\\' + today)
                            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                                os.makedirs(
                                    configContent[
                                        'Reach_Result_Export_URL'] + '\\' + today)  # makedirs 创建文件时如果路径不存在会创建这个路径
                            fileName = configContent[
                                           'Reach_Result_Export_URL'] + '\\' + today + '\\' + 'SVHC ' + name + '.txt'
                            with open(fileName, "w", encoding="utf-8") as fileTxt:
                                for i in range(len(resultDcuOne)):
                                    if i == 0:
                                        lineTxt = str(resultDcuOne[i]) + '\t' + str(resultDcuTwo[i]) + '\t' + str(
                                            resultDcuThree[i]) + '\t' + str(resultDcuFour[i]) + '\t' + str(
                                            resultDcuFive[i]) + '\t' + str(resultDcuSix[i]) + '\n'
                                    else:
                                        lineTxt = str(resultDcuOne[i]) + '\t' + str(resultDcuTwo[i]) + '\t' + str(
                                            resultDcuThree[i]) + '\t' + str(
                                            '%f' % (float(resultDcuFour[i]))) + '\t' + str(
                                            resultDcuFive[i]) + '\t' + str(resultDcuSix[i]) + '\n'
                                    fileTxt.write(lineTxt)
                            wb.SaveAs('%s\\%s\\SVHC %s' % (configContent['Reach_Result_Export_URL'], today, name))
                            n += 1
                        excel.Quit()
                        self.textBrowser.append("完成Reach结果转换为TXT")
                        self.textBrowser.append("生成路径：%s\\%s" % (configContent['Reach_Result_Export_URL'], today))
                        self.lineEdit_6.setText("完成Reach结果转换为TXT")

    def zjyResultToIcp(self):
        # 质检院结果转化为ICP格式
        # 判断是否选择了Result文件
        try:
            selectResultFile[0]
        except NameError:
            m = 'N'
        else:
            if selectResultFile[0] == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Result数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getResult(self, 'ICP')
                if selectResultFile[0] == []:
                    self.lineEdit_6.setText("请重新选择ECO Result数据文件")
                    self.textBrowser.append("请重新选择ECO Result数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择ECO Result数据文件")
                self.textBrowser.append("请重新选择ECO Result数据文件")
                m = 'N'
        if m == 'Y':
            # 判断ECO存储路径是否存在
            fileUrl = configContent['ECO_Result_Export_URL']
            folder = os.path.exists(fileUrl)
            if not folder:
                QMessageBox.information(self, "ECO存储路径出错",
                                        "没有ECO结果转化为TXT的存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nECO_Result_Export_URL",
                                        QMessageBox.Yes)
                self.textBrowser.append("请更改配置文件并导入后，重新选择ECO ZJY Result数据文件")
            else:
                fileNum = 1
                for files in selectResultFile[0]:  # 遍历所有文件
                    # print(os.path.split(files))
                    fileName = os.path.split(files)[1]  # 文件名
                    if fileName.split('.')[-1] != 'csv':
                        reply = QMessageBox.question(self, '信息',
                                                     'Result文件不是ECO质检院的CSV结果文件，\n是否需要获取ECO质检院Result数据文件，CSV格式',
                                                     QMessageBox.Yes | QMessageBox.No,
                                                     QMessageBox.Yes)
                        if reply == QMessageBox.Yes:
                            Ui_MainWindow.getResult(self, 'ICP')
                            self.textBrowser.append("请重新点击ECO ZJY Result按钮开始数据处理")
                        else:
                            self.lineEdit_6.setText("请重新选择ECO的质检院结果数据文件，TXT格式")
                            self.textBrowser.append("请重新选择ECO的质检院结果数据文件，TXT格式")
                    else:
                        self.textBrowser.append("正在进行ECO ZJY转换")
                        self.textBrowser.append("%s:%s" % (fileNum,fileName))
                        fileNum += 1
                        app.processEvents()
                        filePath = files
                        folder = os.path.exists(configContent['ECO_Result_Export_URL'] + '\\' + today)
                        # print(folder)
                        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                            os.makedirs(
                                configContent['ECO_Result_Export_URL'] + '\\' + today)  # makedirs 创建文件时如果路径不存在会创建这个路径
                        filePath2 = configContent['ECO_Result_Export_URL'] + '\\' + today + '\\' + fileName.split('.')[0]
                        csvFile = pd.read_csv(filePath,encoding='gbk', names = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56'])
                        dataResult = csvFile.loc[1]
                        i = 0
                        dropC = []
                        leaveC = []
                        for each in dataResult:
                            if each == '样品名称':
                                leaveC.append(str(i))
                            elif each == '浓度 [ ug/L ]' and '内标' not in list(csvFile.loc[0])[i]:
                                leaveC.append(str(i))
                            else:
                                dropC.append(str(i))
                            i += 1
                        csvFile = csvFile.drop(dropC, axis=1)
                        oneRow = csvFile.loc[0]
                        element = []
                        for each in oneRow:
                            if pd.isnull(each):
                                element.append('')
                            else:
                                element.append(each.split(' ')[2])
                        labNum = list(csvFile[leaveC[0]])
                        starNum = labNum.index('样品名称')+1
                        dataOne = ['Solution Label']
                        dataTwo = ['Type']
                        dataThree = ['Element']
                        dataFour = ['Soln Conc']
                        dataFive = ['Units']
                        dataSix = ['强度']
                        dataSeven = ['重复项']
                        m = starNum
                        for i in range(len(labNum)-starNum):
                            for n in range(len(leaveC)):
                                dataOne.append(labNum[m])
                                dataTwo.append('样品')
                                dataFive.append('ug/L')
                                dataSix.append('')
                                dataSeven.append('')
                            dataThree += element
                            data = list(csvFile.loc[m])
                            dataFour += list(csvFile.loc[m])
                            m += 1
                        resultData = pd.DataFrame(
                            {'a': dataOne, 'b': dataTwo, 'c': dataThree, 'd': dataFour, 'e': dataFive, 'f': dataSix, 'g': dataSeven})
                        resultData.to_csv('%s.txt'% filePath2, sep='\t', index=0, header=0)
                    self.textBrowser.append("完成ECO ZJY转换")

    def icpQc(self):
        # ICP QC 填写
        # 判断是否选择了Result文件
        # 判断是否选择了Result文件
        try:
            selectResultFile[0]
        except NameError:
            m = 'N'
        else:
            if selectResultFile[0] == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Result数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getResult(self, 'ICP')
                if selectResultFile[0] == []:
                    self.lineEdit_6.setText("请重新选择ICP Result数据文件")
                    self.textBrowser.append("请重新选择ICP Result数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择ICP Result数据文件")
                self.textBrowser.append("请重新选择ICP Result数据文件")
                m = 'N'
        if m == 'Y':
            # 判断ICP QC模板是否存在
            file = configContent['ICP_QC_Chart_Import_URL'] + '\\' + configContent['ICP_QC_Chart_File_Name']
            folder = os.path.exists(file)
            if not folder:
                QMessageBox.information(self, "无ICP QC模板",
                                        "没有QC Chart模板文件！！！\n请查看config配置文件内容是否符合需求。\nICP_QC_Chart_Import_URL,ICP_QC_Chart_File_Name\nICP QC Chart的文件路径、文件名称和Excel格式",
                                        QMessageBox.Yes)
                self.textBrowser.append("请更改配置文件并导入后，重新点击MM QC Chart按钮开始数据处理")
            else:
                excel = win32com.gencache.EnsureDispatch('Excel.Application')
                excel.Visible = True
                excel.Application.DisplayAlerts = True
                wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s\%s' % (
                    configContent['ICP_QC_Chart_Import_URL'], configContent['ICP_QC_Chart_File_Name'])))
                ws = wb.Worksheets('Data')
                x = 1
                oneRow = []
                while ws.Cells(1, x).Value is not None:
                    oneRow.append(ws.Cells(1, x).Value)
                    x += 1
                materialColumn = int(oneRow.index('Material')) + 1
                sampleColumn = int(oneRow.index('Element')) + 1
                material = []
                resultRows = {}
                elements = []
                n = 2
                # 获取需要测试元素
                while ws.Cells(n, materialColumn).Value is not None:
                    material.append(ws.Cells(n, materialColumn).Value)
                    elements.append(ws.Cells(n, sampleColumn).Value)
                    resultRows['%s-%s' % (ws.Cells(n, materialColumn).Value, ws.Cells(n, sampleColumn).Value)] = n
                    n += 1
                # print(elements)
                # 获取所需数据
                rusultList = []
                rusultList2 = []
                rusultList3 = []
                e = str()
                m = []
                for each in set(material):
                    m.append(each)
                for each in m:
                    if each == m[-1]:
                        e = e + each
                    else:
                        e = e + each + '|'
                y = 1
                for fileUrl in selectResultFile[0]:  # 遍历结果选择文件
                    fileDate = os.path.split(fileUrl)[1].split('-')[0]
                    self.textBrowser.append("%s:%s" % (y,fileDate))
                    self.lineEdit_6.setText("正在进行%s QC填写" % fileDate)
                    app.processEvents()
                    # 获取相关结果数据
                    csvFile = pd.read_csv(fileUrl, header=0, names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
                    csvFile.drop(['B', 'C', 'F', 'G', 'H'], axis=1, inplace=True)# 保留A,D,E列
                    csvFile = csvFile.loc[csvFile['A'].str.contains(e)]# 保留material列，不重复的物质
                    csvFile = csvFile[csvFile['D'].isin(set(elements))]# 保留不重复元素
                    rusultList = list(csvFile['A'])
                    rusultList2 = list(csvFile['D'])
                    rusultList3 = list(csvFile['E'])
                    # print(resultRows)
                    for num in resultRows:
                        # print(num,resultRows[num])
                        if 'Date' in num:  # 跳过填写日期的行
                            continue
                        else:
                            c = 6
                            while ws.Cells(resultRows[num], c).Value is not None:
                                c += 1
                            for i in range(len(rusultList)):  # 遍历结果列表
                                list1 = rusultList[i].split(',')
                                if '%s-%s' % (list1[0], rusultList2[i]) in num:
                                    if i + 1 < len(rusultList):
                                        # 相同的元素测试验证并跳过
                                        if '%s-%s' % (rusultList[i], rusultList2[i]) == '%s-%s' % (
                                                rusultList[i + 1], rusultList2[i + 1]):
                                            continue
                                    if ',' in rusultList[i]:  # 将需要计算的挑选出来
                                        if len(list1) == 3:
                                            # float(rusultList3[i])*int(float(list1[1])*250)*float(list1[2])/float(list1[1])---溶度*定容体积*稀释倍数/质量
                                            ws.Cells(resultRows['%s-%s' % (list1[0], rusultList2[i])],
                                                     c).Value = float(
                                                rusultList3[i]) * int(float(list1[1]) * 250) * float(
                                                list1[2]) / float(
                                                list1[1])
                                        elif len(list1) == 2:
                                            ws.Cells(resultRows['%s-%s' % (list1[0], rusultList2[i])],
                                                     c).Value = float(
                                                rusultList3[i]) * int(float(list1[1]) * 250) / float(list1[1])
                                    else:
                                        if 'Date-%s' % rusultList[i] in resultRows.keys():  # 根据是否含有该索引填写日期
                                            ws.Cells(resultRows['Date-%s' % rusultList[i]], c).Value = fileDate
                                        ws.Cells(resultRows['%s-%s' % (rusultList[i], rusultList2[i])], c).Value = \
                                            rusultList3[i]
                                    c += 1
                    y += 1
                self.textBrowser.append("完成QC填写")
                self.lineEdit_6.setText("完成QC填写")

    def resultZjyToTxt(self):
        # 质检院结果科学计数法转化为自然数法
        # 判断是否选择了Result文件
        try:
            selectResultFile[0]
        except NameError:
            m = 'N'
        else:
            if selectResultFile[0] == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Result数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getResult(self, 'ICP')
                if selectResultFile[0] == []:
                    self.lineEdit_6.setText("请重新选择ICP Result数据文件")
                    self.textBrowser.append("请重新选择ICP Result数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择ICP Result数据文件")
                self.textBrowser.append("请重新选择ICP Result数据文件")
                m = 'N'
        if m == 'Y':
            # 判断ECO存储路径是否存在
            fileUrl = configContent['ECO_Result_Export_URL']
            folder = os.path.exists(fileUrl)
            if not folder:
                QMessageBox.information(self, "ECO存储路径出错",
                                        "没有ECO结果转化为TXT的存储文件路径！！！\n请查看config配置文件内容是否符合需求。\nECO_Result_Export_URL",
                                        QMessageBox.Yes)
                self.textBrowser.append("请更改配置文件并导入后，重新选择ECO ZJY Result数据文件")
            else:
                for files in selectResultFile[0]:  # 遍历所有文件
                    # print(os.path.split(files))
                    fileName = os.path.split(files)[1]  # 文件名
                    if fileName.split('.')[-1] != 'txt':
                        reply = QMessageBox.question(self, '信息',
                                                     'Result文件不是ECO质检院的TXT结果文件，\n是否需要获取ECO质检院Result数据文件，TXT格式',
                                                     QMessageBox.Yes | QMessageBox.No,
                                                     QMessageBox.Yes)
                        if reply == QMessageBox.Yes:
                            Ui_MainWindow.getResult(self, 'ICP')
                            self.textBrowser.append("请重新点击ECO ZJY Result按钮开始数据处理")
                        else:
                            self.lineEdit_6.setText("请重新选择ECO的质检院结果数据文件，TXT格式")
                            self.textBrowser.append("请重新选择ECO的质检院结果数据文件，TXT格式")
                    else:
                        self.textBrowser.append("正在进行%s ECO ZJY转换" % fileName)
                        app.processEvents()
                        filePath = files
                        folder = os.path.exists(configContent['ECO_Result_Export_URL'] + '\\' + today)
                        # print(folder)
                        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                            os.makedirs(
                                configContent['ECO_Result_Export_URL'] + '\\' + today)  # makedirs 创建文件时如果路径不存在会创建这个路径
                        filePath2 = configContent['ECO_Result_Export_URL'] + '\\' + today + '\\' + fileName
                        with open(filePath, "r", encoding="utf-8") as f1, open(filePath2, "w", encoding="utf-8") as f2:
                            for line in f1:
                                oldStr = re.findall("\d{1,2}.\d{1,4}E.*\d{1,4} ug/l", line)
                                # print(line)
                                # print(oldStr)
                                if oldStr != []:
                                    newStr = '    ' + '%f'%(float(oldStr[0].split(' ')[0])) + ' ' + 'ug/l'
                                    # print(newStr,oldStr[0].split(' ')[0],'%f'%(float(oldStr[0].split(' ')[0])))
                                    line = line.replace(oldStr[0], newStr)
                                f2.write(line)
                        self.textBrowser.append("完成%s ECO ZJY转换" % fileName)
                        app.processEvents()
                    self.textBrowser.append("生成路径：%s\\%s" % (configContent['ECO_Result_Export_URL'], today))
                    self.lineEdit_6.setText("完成ECO ZJY转换")

    def uvQc(self,messages):
        # 判断是否选择了Result文件
        try:
            selectResultFile[0]
        except NameError:
            m = 'N'
        else:
            if selectResultFile[0] == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Result数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getResult(self, 'UV')
                if selectResultFile[0] == []:
                    self.lineEdit_6.setText("请重新选择UV Result数据文件")
                    self.textBrowser_5.append("请重新选择UV Result数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择UV Result数据文件")
                self.textBrowser_5.append("请重新选择UV Result数据文件")
                m = 'N'
        if m == 'Y':
            # 判断UV QC模板是否存在
            if messages == 'Formal':
                fileName = configContent['Formal_QC_Chart_File_Name']
            elif messages == 'Cr VI':
                fileName = configContent['Cr_VI_QC_Chart_File_Name']
            file = configContent['UV_QC_Chart_Import_URL'] + '\\' + fileName
            folder = os.path.exists(file)
            if not folder:
                QMessageBox.information(self, "无UV QC模板",
                                        "没有QC Chart模板文件！！！\n请查看config配置文件内容是否符合需求。\nUV_QC_Chart_Import_URL,Formal_QC_Chart_File_Name,Cr_VI_QC_Chart_File_Name;\nUV QC Chart的文件路径、对应方法、文件名称和Excel格式",
                                        QMessageBox.Yes)
                self.textBrowser_5.append("请更改配置文件并导入后，重新点击QC Chart按钮开始数据处理")
            else:
                self.textBrowser_5.append("正在进行QC Chart填写")
                excel = win32com.gencache.EnsureDispatch('Excel.Application')
                excel.Visible = True
                excel.Application.DisplayAlerts = True
                wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % file))
                ws = wb.Worksheets('Data')
                x = 1
                oneRow = []
                while ws.Cells(1, x).Value is not None:
                    oneRow.append(ws.Cells(1, x).Value)
                    x += 1
                materialColumn = int(oneRow.index('Material')) + 1
                sampleColumn = int(oneRow.index('Chemical Name')) + 1
                material = []
                resultRows = {}
                elements = []
                n = 2
                # 获取需要测试元素
                while ws.Cells(n, materialColumn).Value is not None:
                    material.append(ws.Cells(n, materialColumn).Value)
                    elements.append(ws.Cells(n, sampleColumn).Value)
                    resultRows['%s-%s' % (ws.Cells(n, materialColumn).Value, ws.Cells(n, sampleColumn).Value)] = n
                    n += 1
                # print(elements)
                # 获取所需数据
                rusultList = []
                rusultList2 = []
                rusultList3 = []
                e = str()
                m = []
                for each in set(material):
                    m.append(each)
                for each in m:
                    if each == m[-1]:
                        e = e + each
                    else:
                        e = e + each + '|'
                y = 1
                for fileUrl in selectResultFile[0]:  # 遍历结果选择文件
                    # 获取相关结果数据
                    try:
                        csvFile = pd.read_csv(fileUrl, header=0, names=['A', 'B', 'C', 'D'])
                    except pd.errors.ParserError:
                        QMessageBox.warning(self, "文件格式错误", "%s文件格式不正确，\n请调整成正确的文件格式后继续操作。"% fileUrl, QMessageBox.Yes)
                        os.startfile(os.path.split(fileUrl)[0])
                        break
                    else:
                        csvFile.drop(['C','D'], axis=1, inplace=True)# 保留A,B,D列
                        dataResult = csvFile.loc[1]
                        fileDate = dataResult[1].split(' ')[0]
                        self.textBrowser_5.append("%s:%s" % (y,fileDate))
                        self.lineEdit_6.setText("正在进行%s QC填写" % fileDate)
                        app.processEvents()
                        csvFile = csvFile.loc[csvFile['A'].str.contains(e,na=False)]# 保留material列，不重复的物质
                        rusultList = list(csvFile['A'])
                        rusultList2 = list(csvFile['B'])
                        for num in resultRows:
                            # print(num,resultRows[num])
                            if 'Date' in num:  # 跳过填写日期的行
                                continue
                            else:
                                c = 6
                                while ws.Cells(resultRows[num], c).Value is not None:
                                    c += 1
                                for i in range(len(rusultList)):  # 遍历结果列表
                                    # print('%s-%s' % (rusultList[i].strip(), messages),num)
                                    if '%s-%s' % (rusultList[i].strip(), messages) in num:# strip()去除空格
                                        if 'Date-%s' % rusultList[i].strip() in resultRows.keys():  # 根据是否含有该索引填写日期
                                            ws.Cells(resultRows['Date-%s' % rusultList[i].strip()], c).Value = fileDate
                                            ws.Cells(resultRows['Date-%s' % rusultList[i].strip()], c).NumberFormat = "yyyy/mm/dd"
                                        if 'QCQ' in rusultList[i].strip() or 'BLK SPIKE' in rusultList[i].strip():
                                            continue
                                        else:
                                            ws.Cells(resultRows['%s-%s' % (rusultList[i].strip(), messages)], c).Value = rusultList2[i].strip()
                                        c += 1
                        y += 1
                self.textBrowser_5.append("完成QC填写")
                self.lineEdit_6.setText("完成QC填写")

    def phQc(self,messages):
        # 判断是否选择了Result文件
        try:
            selectResultFile[0]
        except NameError:
            m = 'N'
        else:
            if selectResultFile[0] == []:
                m = 'N'
            else:
                m = 'Y'
        if m == 'N':
            reply = QMessageBox.question(self, '信息', '是否需要获取Result数据文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getResult(self, 'UV')
                if selectResultFile[0] == []:
                    self.lineEdit_6.setText("请重新选择UV Result数据文件")
                    self.textBrowser_5.append("请重新选择UV Result数据文件")
                    m = 'N'
                else:
                    m = 'Y'
            else:
                self.lineEdit_6.setText("请重新选择pH Result数据文件")
                self.textBrowser_5.append("请重新选择pH Result数据文件")
                m = 'N'
        if m == 'Y':
            # 判断UV QC模板是否存在
            if messages == 'pH 2014':
                fileName = configContent['pH2014_QC_Chart_File_Name']
            elif messages == 'pH 2018':
                fileName = configContent['pH2018_QC_Chart_File_Name']
            file = configContent['UV_QC_Chart_Import_URL'] + '\\' + fileName
            folder = os.path.exists(file)
            if not folder:
                QMessageBox.information(self, "无pH QC模板",
                                        "没有QC Chart模板文件！！！\n请查看config配置文件内容是否符合需求。\nUV_QC_Chart_Import_URL,pH2014_QC_Chart_File_Name,pH2018_QC_Chart_File_Name;\npH QC Chart的文件路径、对应方法、文件名称和Excel格式",
                                        QMessageBox.Yes)
                self.textBrowser_5.append("请更改配置文件并导入后，重新点击QC Chart按钮开始数据处理")
            else:
                self.textBrowser_5.append("正在进行QC Chart填写")
                excel = win32com.gencache.EnsureDispatch('Excel.Application')
                excel.Visible = True
                excel.Application.DisplayAlerts = True
                wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % file))
                ws = wb.Worksheets('Data')
                x = 1
                oneRow = []
                while ws.Cells(1, x).Value is not None:
                    oneRow.append(ws.Cells(1, x).Value)
                    x += 1
                materialColumn = int(oneRow.index('Material')) + 1
                sampleColumn = int(oneRow.index('Chemical Name')) + 1
                material = []
                resultRows = {}
                elements = []
                n = 2
                # 获取需要测试元素
                while ws.Cells(n, materialColumn).Value is not None:
                    material.append(ws.Cells(n, materialColumn).Value)
                    elements.append(ws.Cells(n, sampleColumn).Value)
                    if ws.Cells(n, sampleColumn).Value is None:
                        ws.Cells(n, sampleColumn).Value = 'nan'
                    resultRows['%s-%s' % (ws.Cells(n, materialColumn).Value, ws.Cells(n, sampleColumn).Value)] = n
                    n += 1
                # print(elements)
                # 获取所需数据
                rusultList = []
                rusultList2 = []
                rusultList3 = []
                e = str()
                m = []
                for each in set(material):
                    m.append(each)
                for each in m:
                    if each == m[-1]:
                        e = e + each
                    else:
                        e = e + each + '|'
                y = 1
                for fileUrl in selectResultFile[0]:  # 遍历结果选择文件
                    # 获取相关结果数据
                    try:
                        csvFile = pd.read_csv(fileUrl, header=0, names=['A', 'B', 'C', 'D','E','F','G','H','I','J'])
                    except pd.errors.ParserError:
                        QMessageBox.warning(self, "文件格式错误", "%s文件格式不正确，\n请调整成正确的文件格式后继续操作。"% fileUrl, QMessageBox.Yes)
                        os.startfile(os.path.split(fileUrl)[0])
                        break
                    else:
                        csvFile.drop(['B','E','G','H','I','J'], axis=1, inplace=True)  # 保留A,B,D列
                        dataResult = csvFile.loc[1]
                        fileDate = dataResult[0].split(' ')[0]
                        csvFile.drop(['A'], axis=1, inplace=True)
                        self.textBrowser_5.append("%s:%s" % (y, fileDate))
                        self.lineEdit_6.setText("正在进行%s QC填写" % fileDate)
                        app.processEvents()
                        csvFile = csvFile.loc[csvFile['C'].str.contains(e, na=False)]  # 保留material列，不重复的物质
                        rusultList = list(csvFile['C'])
                        rusultList2 = list(csvFile['D'])
                        rusultList3 = list(csvFile['F'])
                        for num in resultRows:
                            # print(num,resultRows[num])
                            if 'Date' in num:  # 跳过填写日期的行
                                continue
                            else:
                                c = 6
                                while ws.Cells(resultRows[num], c).Value is not None:
                                    c += 1
                                for i in range(len(rusultList)):  # 遍历结果列表
                                    # print('%s-%s' % (rusultList[i], rusultList2[i]),num)
                                    if '%s-%s' % (rusultList[i], rusultList2[i]) in num:  # strip()去除空格
                                        if 'Date-%s' % rusultList[i] in resultRows.keys():  # 根据是否含有该索引填写日期
                                            ws.Cells(resultRows['Date-%s' % rusultList[i]], c).Value = fileDate
                                            ws.Cells(resultRows['Date-%s' % rusultList[i]], c).NumberFormat = "yyyy/mm/dd"
                                        ws.Cells(resultRows['%s-%s' % (rusultList[i], rusultList2[i])], c).Value = \
                                        rusultList3[i]
                                        c += 1
                        y += 1
                self.textBrowser_5.append("完成QC填写")
                self.lineEdit_6.setText("完成QC填写")

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
            self.lineEdit_6.setText("Reach信息获取成功")

    def searchReachMessage(self):
        # 搜索Reach信息提示
        try:
            reachLimsNo
        except NameError:
            reply = QMessageBox.question(self, '信息', '是否需要获取Reach信息文件', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                Ui_MainWindow.getReachMessage(self)
                self.lineEdit_6.setText("请继续点击搜索按钮以搜索Reach信息")
            else:
                self.lineEdit_6.setText("请点击获取按钮以取得Reach信息")
        else:
            reachContent = self.lineEdit_4.text()
            reachNum = self.spinBox_6.text()
            # print(type(reachContent),1,type(reachNum))
            if (reachContent == '') and (reachNum == '0'):
                self.lineEdit_6.setText("请输入需要查找Reach英文内容或者编号")
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
                self.lineEdit_6.setText("搜索完成")

    def getData(self, pbt):
        # 自动填写-获取填写内容
        text = self.lineEdit.text() + pbt.text()
        self.lineEdit.setText(text)
        self.lineEdit_6.setText("内容已填写，可随时开始")

        # 自动填写-清除内容

    def clearContent(self):
        # 清除填写内容
        self.lineEdit.clear()
        self.lineEdit_6.setText("已清零，请重新填写内容")

    def stopMessage(self):
        # 自动填写-停止
        stopMessage1 = 'stop'
        self.lineEdit.setText(stopMessage1)
        self.lineEdit_6.setText("已停止，请清零后重新开始!!!")

    def autoWrite(self):
        # 自动填写 - 开始自动填写
        if self.lineEdit.text() == '' or self.lineEdit.text() == 'stop':
            QMessageBox.information(self, "提示信息", "自动填写中无内容或内容为‘stop’，请清零并填写内容",
                                    QMessageBox.Yes)
        else:
            time.sleep(3)
            n = int(self.spinBox.text())
            if self.lineEdit.text() == 'Sample ID':
                self.lineEdit_6.setText("正在填写样品单号")
                for each in labNumber:
                    if self.lineEdit.text() != 'stop':
                        pyautogui.typewrite('%s' % each, 0.0001)
                        pyautogui.typewrite(['Enter'])
                        app.processEvents()
                        time.sleep(0.1)
            elif self.lineEdit.text() == 'Random':
                for i in range(n):
                    if self.lineEdit.text() != 'stop':
                        pyautogui.typewrite(
                            '%s' % random.randint(int(self.spinBox_4.text()), int(self.spinBox_5.text())),
                            0.0001)
                        pyautogui.typewrite(['Enter'])
                        app.processEvents()
                        time.sleep(0.1)
            else:
                self.lineEdit_6.setText("正在自动填写内容")
                for i in range(n):
                    if self.lineEdit.text() != 'stop':
                        pyautogui.typewrite('%s' % self.lineEdit.text(), 0.0001)
                        pyautogui.typewrite(['Enter'])
                        app.processEvents()
                        time.sleep(0.1)
                if self.lineEdit.text() != 'stop':
                    self.lineEdit_6.setText("自动填写已经完成")

    def randomAction(self):
        # 自动填写-随机数
        self.lineEdit.setText('Random')
        self.lineEdit_6.setText("随时可以开始填写随机数")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "操作界面"))
        MainWindow.setStatusTip(_translate("MainWindow", "作者：Frank Chen"))
        self.pushButton_28.setText(_translate("MainWindow", "信息："))
        self.pushButton_29.setStatusTip(_translate("MainWindow", "选择需要获取的Batch"))
        self.pushButton_29.setText(_translate("MainWindow", "选择Batch"))
        self.pushButton_22.setStatusTip(_translate("MainWindow", "获取Sample ID，并填入Excel模板中"))
        self.pushButton_22.setText(_translate("MainWindow", "Nickel Batch"))
        self.pushButton_23.setStatusTip(_translate("MainWindow", "由于AAS仪器中有些Bug只能识别‘-’，所以需获取Sample ID，并将‘+’改为‘-’"))
        self.pushButton_23.setText(_translate("MainWindow", "AAS Batch"))
        self.textBrowser_3.setStatusTip(_translate("MainWindow", "选择Barch的文件信息"))
        self.pushButton_24.setStatusTip(_translate("MainWindow", "获取Sample ID，按中迅德要求生成Batch单"))
        self.pushButton_24.setText(_translate("MainWindow", "ECO ZXD"))
        self.pushButton_25.setStatusTip(_translate("MainWindow", "获取Sample ID，生成符合质检院的单号同时生产出打印编号"))
        self.pushButton_25.setText(_translate("MainWindow", "ECO ZJY"))
        self.pushButton_35.setText(_translate("MainWindow", "起始编号"))
        self.pushButton_36.setText(_translate("MainWindow", "结尾编号"))
        self.pushButton_33.setText(_translate("MainWindow", "信息："))
        self.pushButton_34.setStatusTip(_translate("MainWindow", "选择需要获取的Resutl数据"))
        self.pushButton_34.setText(_translate("MainWindow", "选择Result"))
        self.spinBox_3.setStatusTip(_translate("MainWindow", "Reach结果第几个开始生成"))
        self.spinBox_2.setStatusTip(_translate("MainWindow", "Reach结果第几个结束，同时0表示该Batch最后一个"))
        self.textBrowser.setStatusTip(_translate("MainWindow", "选择Result的文件信息"))
        self.pushButton_38.setStatusTip(_translate("MainWindow", "获取Sample ID和结果数据，并填入Reach结果Excel模板中 "))
        self.pushButton_38.setText(_translate("MainWindow", "Reach Result"))
        self.pushButton_27.setStatusTip(_translate("MainWindow", "将CSV转化成DCU使用的TXT格式"))
        self.pushButton_27.setText(_translate("MainWindow", "ICP Result"))
        self.pushButton_31.setStatusTip(_translate("MainWindow", "由于质检院仪器结果导出不符合DCU格式，需要转化为ICP结果格式"))
        self.pushButton_31.setText(_translate("MainWindow", "ECO ZJY To ICP"))
        self.pushButton_30.setStatusTip(_translate("MainWindow", "填写ICP的QC Chart"))
        self.pushButton_30.setText(_translate("MainWindow", "MM QC Chart"))
        self.comboBox.setStatusTip(_translate("MainWindow", "Result数据的选择路径"))
        self.comboBox.setItemText(0, _translate("MainWindow", "URL:ICP Result"))
        self.comboBox.setItemText(1, _translate("MainWindow", "URL:ECO ZJY Result"))
        self.pushButton_32.setStatusTip(_translate("MainWindow", "由于质检院结果是科学计数法导致有些结果无法DCU，所以需要将结果转化"))
        self.pushButton_32.setText(_translate("MainWindow", "ECO ZJY Result"))
        self.pushButton_21.setStatusTip(_translate("MainWindow", "获取Sample ID，并导出TXT"))
        self.pushButton_21.setText(_translate("MainWindow", "ICP Batch"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ICP Operate"))
        self.spinBox_6.setStatusTip(_translate("MainWindow", "Reach中Lims中的物质编号"))
        self.pushButton_40.setText(_translate("MainWindow", "物质编号"))
        self.textBrowser_2.setStatusTip(_translate("MainWindow", "物质信息显示区域"))
        self.pushButton_37.setStatusTip(_translate("MainWindow", "根据内容或编号查找Reach物质的信息"))
        self.pushButton_37.setText(_translate("MainWindow", "搜索"))
        self.lineEdit_5.setStatusTip(_translate("MainWindow", "物质中文名字显示区域"))
        self.pushButton_51.setStatusTip(_translate("MainWindow", "将所有之前查找的信息清除"))
        self.pushButton_51.setText(_translate("MainWindow", "清零"))
        self.pushButton_50.setStatusTip(_translate("MainWindow", "获取Reach物质信息"))
        self.pushButton_50.setText(_translate("MainWindow", "获取"))
        self.lineEdit_4.setStatusTip(_translate("MainWindow", "输入Reach物质的内容"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Reach Message"))
        self.pushButton_19.setText(_translate("MainWindow", "内容："))
        self.lineEdit.setStatusTip(_translate("MainWindow", "填写内容显示区域"))
        self.pushButton_20.setText(_translate("MainWindow", "次数："))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_10.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_11.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "."))
        self.pushButton_17.setText(_translate("MainWindow", "%"))
        self.spinBox.setStatusTip(_translate("MainWindow", "内容重复填写的次数，Batch填写无效"))
        self.pushButton_13.setText(_translate("MainWindow", "Negative"))
        self.pushButton_14.setText(_translate("MainWindow", "Positive"))
        self.pushButton_18.setStatusTip(_translate("MainWindow", "选择需要获取的Batch"))
        self.pushButton_18.setText(_translate("MainWindow", "选择Batch"))
        self.pushButton_16.setStatusTip(_translate("MainWindow", "内容出现Stop，将停止自动填写"))
        self.pushButton_16.setText(_translate("MainWindow", "停止"))
        self.spinBox_5.setStatusTip(_translate("MainWindow", "随机数最大值"))
        self.spinBox_4.setStatusTip(_translate("MainWindow", "随机数最小值"))
        self.pushButton_26.setStatusTip(_translate("MainWindow", "点击后将以随机数的形式填写"))
        self.pushButton_26.setText(_translate("MainWindow", "随机数"))
        self.pushButton_15.setStatusTip(_translate("MainWindow", "清零后才可开始新的填写"))
        self.pushButton_15.setText(_translate("MainWindow", "清零"))
        self.pushButton.setStatusTip(_translate("MainWindow", "开始后，你将有几秒钟时间选择起始位置"))
        self.pushButton.setText(_translate("MainWindow", "开始\n""填写"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Auto"))
        self.pushButton_44.setStatusTip(_translate("MainWindow", "获取Sample ID以甲醛格式生成TXT格式"))
        self.pushButton_44.setText(_translate("MainWindow", "Formal Batch"))
        self.textBrowser_4.setStatusTip(_translate("MainWindow", "选择Barch的文件信息"))
        self.pushButton_39.setText(_translate("MainWindow", "信息："))
        self.pushButton_41.setStatusTip(_translate("MainWindow", "选择需要获取的Batch"))
        self.pushButton_41.setText(_translate("MainWindow", "选择Batch"))
        self.pushButton_48.setStatusTip(_translate("MainWindow", "填写pH QC Chart"))
        self.pushButton_48.setText(_translate("MainWindow", "pH QC 2014"))
        self.pushButton_45.setStatusTip(_translate("MainWindow", "获取Sample ID以pH格式生成CSV格式"))
        self.pushButton_45.setText(_translate("MainWindow", "pH Batch"))
        self.pushButton_42.setText(_translate("MainWindow", "信息："))
        self.pushButton_43.setStatusTip(_translate("MainWindow", "选择Result文件"))
        self.pushButton_43.setText(_translate("MainWindow", "选择Result"))
        self.pushButton_46.setStatusTip(_translate("MainWindow", "获取Sample ID以六价铬格式生成TXT格式"))
        self.pushButton_46.setText(_translate("MainWindow", "Cr VI Batch"))
        self.comboBox_2.setStatusTip(_translate("MainWindow", "Result数据的选择路径"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "URL:Formal Result"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "URL:Cr VI Result"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "URL:pH 2018 Result"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "URL:pH 2014 Result"))
        self.textBrowser_5.setStatusTip(_translate("MainWindow", "选择Result的文件信息"))
        self.pushButton_47.setStatusTip(_translate("MainWindow", "填写甲醛QC Chart"))
        self.pushButton_47.setText(_translate("MainWindow", "Formal QC"))
        self.pushButton_49.setStatusTip(_translate("MainWindow", "填写六价铬QC Chart"))
        self.pushButton_49.setText(_translate("MainWindow", "Cr VI QC"))
        self.pushButton_52.setText(_translate("MainWindow", "pH QC 2018"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "UV Operate"))
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

if __name__ == "__main__":
    import sys
    import os
    import time
    import random
    import pyautogui
    import pandas as pd
    import re
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