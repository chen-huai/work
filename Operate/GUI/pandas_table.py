"""
有趣的事情
没有结束
2020/4/17 10:14
"""
import pandas as pd
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import chicon  # 引用图标
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QTableView)
from PyQt5.QtCore import (QAbstractTableModel, Qt)
from pandas_table import *
from TableView_Ui import *

class MyTableWindow(QMainWindow, Ui_TableWindow):
    def __init__(self, parent=None):
        super(MyTableWindow, self).__init__(parent)
        self.setupUi(self)
    def data(self):
        data = {'性别': ['男', '女', '女', '男', '男'],
                '姓名': ['小明', '小红', '小芳', '小强', '小美'],
                '年龄': [20, 21, 25, 24, 29]}
        df = pd.DataFrame(data, index=['No.1', 'No.2', 'No.3', 'No.4', 'No.5'],
                          columns=['姓名', '性别', '年龄', '职业'])

        model = PdTable(df)
        self.tableView.setModel(model)
        self.tableView.setAlternatingRowColors(True)

class PdTable(QAbstractTableModel):
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

    # 显示行和列头
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][col]
        return None


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    data = {'性别': ['男', '女', '女', '男', '男'],
            '姓名': ['小明', '小红', '小芳', '小强', '小美'],
            '年龄': [20, 21, 25, 24, 29]}
    df = pd.DataFrame(data, index=['No.1', 'No.2', 'No.3', 'No.4', 'No.5'],
                      columns=['姓名', '性别', '年龄', '职业'])

    model = PdTable(df)
    ui = MyTableWindow()
    ui.show()
    # view = QTableView()
    # view.setModel(model)
    # view.setWindowTitle('Pandas')
    # view.resize(900, 550)
    # view.setAlternatingRowColors(True)
    # view.show()
    ui.data()
    sys.exit(app.exec_())