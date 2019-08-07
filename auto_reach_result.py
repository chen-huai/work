#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pyautogui
import os
import os.path
import openpyxl
import easygui as g
from win32com.client import Dispatch
import win32com.client as win32com
now_1 = str(time.strftime('%Y'))
list=[]
id_number=[]
pyautogui.PAUSE=1
pyautogui.FAILSAFE= True 
print(pyautogui.size())
print(pyautogui.position())

path=g.fileopenbox(msg=None,title=None,default='Z:/Data/%s/66-01-2018-012 ICP-OES/SVHC'%now_1,filetypes=None) 
excel = win32com.gencache.EnsureDispatch('Excel.Application')
excel.Visible = True
excel.Application.DisplayAlerts = True   
workbook = excel.Workbooks.Open(os.path.join(os.getcwd(),r'%s'%path))

time.sleep(10)
row=5
x=117
print()
while excel.Sheets('SVHC-181').Cells(x,11).Value is not None:
    x+=1  
for i in range(x-5):
    result=round(excel.Sheets("SVHC-181").Cells(row,11).Value,3)
    id_no=excel.Sheets("SVHC-181").Cells(row,1).Value
    list.append(result)
    id_number.append(id_no)
    i+=1
    row+=1   
m=0
for n in range(len(list)-1):
    if m+1<len(list):
        while id_number[m]==id_number[m+1]:
            if str(list[m])=='-2146826273':  
                m+=1      
            else:
                if str(list[m+1])=='-2146826273':
                    list[m+1]=list[m]
                else:
                    list[m+1]=min(list[m],list[m+1])
            m+=1  
            n+=1  
        pyautogui.typewrite('%s'%list[m],0.0000000001)
        pyautogui.typewrite(['down']) 
        time.sleep(3)        
    else:
        time.sleep(2)
        pyautogui.typewrite(['right']*6)
        pyautogui.typewrite('%s'%id_number[m],0.0000000001)
    m+=1
    n+=1
    