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
now_1 = str(time.strftime('%Y'))
def get_list():  
    lab_number = input('please fill in the lab number:')
    quality=float(input('please fill in the sample quality:'))
    volume=float(input('please fill in 体积:'))
    print ('begin')
    print ('Wait for a moment')
    name = lab_number.replace('/', '_') 
    elements=['Zn','B','As','Sb','Cr','Pb','Co','Ba','Sn','Mo','Zr','Al','Cd','Na','Sr']
    wavelenths=['202.548','249.772','188.980','206.834','267.716','220.353','228.615','230.424','189.925','202.032','343.823','236.705','228.802','589.592','460.733']
    rows=['3','4','5','6','7','8','9','11','12','13','14','15','17','18','20']
    n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    lines= csv.reader(open(path,"rt",encoding='utf-8'))
    lists=[]
    for l in lines:
        lists.append(l) 
    excel = win32com.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    excel.Application.DisplayAlerts = True    
    workbook = excel.Workbooks.Open(os.path.join(os.getcwd(),r'./SVHC.xlsx'))
    for i in range(15):
        list=[]
        m=0
        for line in lists:
            if ('%s'%lab_number in line[0]) and ('%s'%elements[i] in line[2]) and ('(ref)' not in line[2]):                         
                list.append(line) 
            m+=1
        excel.Sheets("1").Cells(rows[i],15).Value=elements[i]
        if list!=[]:
            if str(list[0][4])=='未校正':
                excel.Sheets("1").Cells(rows[i],16).Value='未校正'
            else:
                excel.Sheets("1").Cells(rows[i],16).Value=float(list[0][4])*volume/quality
        else:
            excel.Sheets("1").Cells(rows[i],16).Value='未走标准曲线'
        if n[i]=='15':
            workbook.SaveAs('.\\SVHC %s.xlsx'%name)
            excel.Application.Quit()
        i+=1
path=g.fileopenbox(msg=None,title="Select file",default='Z:/Data/%s/66-01-2018-012 5510 ICP-OES/'%now_1,filetypes=["*.csv"])
get_list()
action=g.ccbox('whether need to run the program again', choices=('continue','finsh'))
while  action==1:
    get_list()
    action=g.ccbox('whether need to run the program again', choices=('continue','finsh'))       
else:    
    os.startfile('.\\')

