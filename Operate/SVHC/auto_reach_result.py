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
import tkinter
now_1 = str(time.strftime('%Y'))
list=[]
id_number=[]
pyautogui.PAUSE=1
pyautogui.FAILSAFE= True 
print(pyautogui.size())
print(pyautogui.position())

path=tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES'%now_1,filetypes=[("file", "*.xls*")])
excel = win32com.gencache.EnsureDispatch('Excel.Application')
excel.Visible = True
excel.Application.DisplayAlerts = True   
workbook = openpyxl.load_workbook(os.path.join(os.getcwd(),'%s'%path))
time.sleep(10)
row=5
x=117
while excel.Sheets('SVHC').Cells(x,11).Value is not None:
    x+=1  
for i in range(x-5):
    result=round(excel.Sheets("SVHC").Cells(row,11).Value,3)
    id_no=excel.Sheets("SVHC").Cells(row,1).Value
    list.append(result)
    id_number.append(id_no)
    i+=1
    row+=1   
m=0
n=0
while n in range(len(list)):
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
        if list[m]<0:
            list[m]=0 
        pyautogui.typewrite('%s'%list[m],0.0000000001)
        pyautogui.typewrite(['down']) 
        time.sleep(3)        
    else:
        pyautogui.typewrite(['Enter'])
        time.sleep(2)
        pyautogui.typewrite(['right']*6)
        pyautogui.typewrite('the end %s'%id_number[m],0.0000000001)
    m+=1
    n+=1