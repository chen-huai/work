#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
import time
import easygui as g
from win32com.client import Dispatch
import win32com.client as win32com
import random
import csv
import tkinter
now_1 = str(time.strftime('%Y'))
t_1 = int(time.strftime('%Y'))
t_2 = t_1-1
now = str(t_1)
last_time = str(t_2)
nowDate = time.strftime('%Y%m%d')
def getSample():
    i = 0
    path = g.fileopenbox(msg=None, title=None, default='Z:/Inorganic_batch/Microwave/batch/*.doc', filetypes=None)

    w = Dispatch('Word.Application')
    w.Visible = 0
    doc = w.Documents.Open(r'%s'%path)
    a = doc.Content.Text
    b = a.split('\r')
    # print(b)
    global labNumber
    global qualityValue
    global volumeValue
    labNumber = []
    qualityValue = []
    volumeValue = []
    i = 0
    for i in range(len(b)):
        if ('/' in b[i]) and (len(b[i]) > 5) and ('/' + last_time not in b[i]) and ('/' + now not in b[i]) and (
                'GB/T' not in b[i]) and ('D' not in b[i]):
            if 'R\x1eI' in b[i+5]:
                labNumber.append(b[i])
                qualityValue.append(b[i+4])
                volumeValue.append(b[i+2])
    # print(labNumber,qualityValue,volumeValue)
def getResult():
    path = tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES/' % now_1,
                                               filetypes=[("csvfile", "*.csv")])
    global resultLists
    lines = csv.reader(open('%s' % path, 'rt', encoding='utf-8'))
    resultLists = []
    for l in lines:
        resultLists.append(l)

def getList():
    print('begin')
    print('Wait for a moment')
    excel = win32com.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    excel.Application.DisplayAlerts = True
    wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'./SVHC.xlsx'))
    elements = []
    resultRows = []
    n = 3
    while wb.Sheets("1").Cells(n, 1).Value is not None:
        elements.append(wb.Sheets("1").Cells(n, 1).Value)
        resultRows.append(n)
        n += 1
    # print(elements)
    for z in range(len(labNumber)):
        wb = excel.Workbooks.Open(os.path.join(os.getcwd(), r'./SVHC.xlsx'))
        name = labNumber[z].replace("/", '_')
        i = 0
        for i in range(len(elements)):
            resultList = []
            for line in resultLists:
                if ('%s' % labNumber[z] in line[0]) and ('%s' % elements[i] in line[3]) and ('(ref)' not in line[3]):
                    resultList.append(line)
            wb.Sheets("1").Cells(resultRows[i], 2).Value = elements[i]
            if resultList != []:
                if str(resultList[0][4]) == '未校正':
                    wb.Sheets("1").Cells(resultRows[i], 3).Value = '未校正'
                elif str(resultList[0][4]) == '####':
                    wb.Sheets("1").Cells(resultRows[i], 3).Value = '超出'
                else:
                    wb.Sheets("1").Cells(resultRows[i], 3).Value = float(resultList[0][4]) * int(volumeValue[z]) / float(qualityValue[z])
            else:
                wb.Sheets("1").Cells(resultRows[i], 3).Value = '未走标准曲线'
            if i == len(elements) - 1:
                wb.Sheets("1").Cells(1, 3).Value = labNumber[z]
                address = os.path.abspath('.')
                wb.SaveAs('%s\\SVHC %s.xlsx' % (address, name))

                time.sleep(1)
        # excel = win32com.gencache.EnsureDispatch('Excel.Application')
        # excel.Visible = True
        # excel.Application.DisplayAlerts = True
        workbookResult = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s\\SVHC %s.xlsx' % (address, name)))
        resultDcuOne = []
        resultDcuTwo = []
        resultDcuThree = []
        resultDcuFour = []
        resultDcuFive = []
        resultDcuSix = []
        m = 1
        while workbookResult.Sheets("DCU-Result").Cells(m, 1).Value is not None:
            resultDcuOne.append(workbookResult.Sheets("DCU-Result").Cells(m, 1).Value)
            resultDcuTwo.append(workbookResult.Sheets("DCU-Result").Cells(m, 2).Value)
            resultDcuThree.append(workbookResult.Sheets("DCU-Result").Cells(m, 3).Value)
            resultDcuFour.append(workbookResult.Sheets("DCU-Result").Cells(m, 4).Value)
            resultDcuFive.append(workbookResult.Sheets("DCU-Result").Cells(m, 5).Value)
            resultDcuSix.append(workbookResult.Sheets("DCU-Result").Cells(m, 6).Value)
            m +=1
        excel.Application.Quit()
        folder = os.path.exists(address + '\\' + nowDate)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(address + '\\' + nowDate)  # makedirs 创建文件时如果路径不存在会创建这个路径
        fileName = address + '\\' + nowDate + '\\' + 'SVHC ' + name + '.txt'
        with open(fileName, "w", encoding="utf-8") as fileTxt:
            for i in range(len(resultDcuOne)):
                lineTxt = str(resultDcuOne[i]) + '\t' + str(resultDcuTwo[i]) + '\t' + str(resultDcuThree[i]) + '\t' + str(resultDcuFour[i]) + '\t' + str(resultDcuFive[i]) + '\t' + str(resultDcuSix[i]) + '\n'
                fileTxt.write(lineTxt)

        z += 1
getSample()
getResult()
getList()
action = g.ccbox('是否需要继续运行此程序', choices=('运行', '取消'))
while action == 1:
    getSample()
    action = g.ccbox('是否需要重新导入结果数据', choices=('需要', '取消'))
    if action == 1:
        getResult()
    getList()
    action = g.ccbox('是否需要继续运行此程序', choices=('运行', '取消'))
else:
    os.startfile('.\\')