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
def get_sample():
    i = 0
    path = g.fileopenbox(msg=None, title=None, default='Z:/Inorganic_batch/Formaldehyde/batch/*.doc', filetypes=None)

    w = Dispatch('Word.Application')
    w.Visible = 0
    doc = w.Documents.Open(r'%s'%path)
    a = doc.Content.Text
    b = a.split('\r')
    #print(b)
    global lab_number,quality,volume
    lab_number = []
    quality = []
    volume = []
    i = 0
    for i in range(len(b)):
        if ('/' in b[i]) and (len(b[i]) > 5) and ('/' + last_time not in b[i]) and ('/' + now not in b[i]) and (
                'GB/T' not in b[i]) and ('D' not in b[i]):
            if 'R-I' in b[i+5]:
                lab_number.append(b[i])
                quality.append(b[i+4])
                volume.append(b[i+2])
    print(lab_number,quality,volume)


def get_list():  
    lab_number = input('please fill in the lab number:')
    quality=float(input('please fill in the sample quality:'))
    volume=float(input('please fill in the volume of the sample:'))
    print ('begin')
    print ('Wait for a moment')
    name = lab_number.replace('/', '_')
    lines = csv.reader(open('%s'%path,'rt',encoding='utf-8'))
    lists = []
    for l in lines:
        lists.append(l)
    excel = win32com.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    excel.Application.DisplayAlerts = True
    workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), r'./SVHC.xlsx'))
    elements = []
    rows = []
    n = 3
    while excel.Sheets("1").Cells(n, 1).Value is not None:
        elements.append(excel.Sheets("1").Cells(n, 1).Value)
        rows.append(n)
        n += 1

    for i in range(len(elements)):
        list = []
        m = 0
        for line in lists:
            if ('%s' % lab_number in line[0]) and ('%s' % elements[i] in line[4]) and ('(ref)' not in line[4]):
                print(line)
                list.append(line)

            m += 1
        excel.Sheets("1").Cells(rows[i], 2).Value = elements[i]
        if list != []:
            if str(list[0][6]) == '未校正':
                excel.Sheets("1").Cells(rows[i], 3).Value = '未校正'
            elif str(list[0][6]) == '####':
                excel.Sheets("1").Cells(rows[i], 3).Value = '超出'
            else:
                excel.Sheets("1").Cells(rows[i], 3).Value = float(list[0][6]) * volume / quality
        else:
            excel.Sheets("1").Cells(rows[i], 3).Value = '未走标准曲线'
        if i == len(elements) - 1:
            address = os.path.abspath('.')
            workbook.SaveAs('%s\\SVHC %s.xlsx' % (address, name))
            excel.Application.Quit()

get_sample()
path = tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES/'%now_1,filetypes=[("csvfile", "*.csv")])

get_list()
action = g.ccbox('whether need to run the program again', choices=('continue', 'finsh'))
while action == 1:
    get_list()
    action = g.ccbox('whether need to run the program again', choices=('continue', 'finsh'))
else:
    os.startfile('.\\')