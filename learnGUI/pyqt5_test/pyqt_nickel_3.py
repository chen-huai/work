# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_nickel_3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import pyautogui
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(160, 329)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 141, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(lambda: self.get_data(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.get_data(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.get_data(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.get_data(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.get_data(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.get_data(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.get_data(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.get_data(self.pushButton_9))
        self.pushButton_10.clicked.connect(lambda: self.get_data(self.pushButton_10))
        self.pushButton_11.clicked.connect(lambda: self.get_data(self.pushButton_11))
        self.pushButton_12.clicked.connect(lambda: self.get_data(self.pushButton_12))
        self.pushButton_13.clicked.connect(lambda: self.get_data(self.pushButton_13))
        self.pushButton_14.clicked.connect(lambda: self.get_data(self.pushButton_14))
        self.pushButton_15.clicked.connect(lambda: self.lineEdit.clear())
        self.pushButton.clicked.connect(self.auto_write)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def get_data(self, pbt):
        text = self.lineEdit.text() + pbt.text()
        self.lineEdit.setText(text)

    def auto_write(self):
        time.sleep(3)
        n=int(self.spinBox.text())
        for i in range(n):
            pyautogui.typewrite('%s' %self.lineEdit.text(),0.0000000001)
            pyautogui.typewrite(['Enter'])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "nickel"))
        self.label.setText(_translate("Dialog", "内容："))
        self.label_2.setText(_translate("Dialog", "次数："))
        self.pushButton_3.setText(_translate("Dialog", "8"))
        self.pushButton_6.setText(_translate("Dialog", "5"))
        self.pushButton_5.setText(_translate("Dialog", "4"))
        self.pushButton_12.setText(_translate("Dialog", "."))
        self.pushButton_7.setText(_translate("Dialog", "6"))
        self.pushButton_2.setText(_translate("Dialog", "7"))
        self.pushButton_10.setText(_translate("Dialog", "3"))
        self.pushButton_11.setText(_translate("Dialog", "0"))
        self.pushButton_4.setText(_translate("Dialog", "9"))
        self.pushButton_9.setText(_translate("Dialog", "2"))
        self.pushButton_8.setText(_translate("Dialog", "1"))
        self.pushButton_13.setText(_translate("Dialog", "Negative"))
        self.pushButton_14.setText(_translate("Dialog", "Positive"))
        self.pushButton_15.setText(_translate("Dialog", "清零"))
        self.pushButton.setText(_translate("Dialog", "开始填写"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Dialog()  # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
