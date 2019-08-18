#!/usr/bin/env python
# -*- coding: utf-8 -*-


 
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import openpyxl
import easygui as g
import os.path
import win32com.client as win32com
import time
import datetime
import calendar
import pyautogui
time_1 = int(time.strftime('%m'))
time_2=calendar.month_abbr[time_1]
address=os.path.abspath('.')
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('作者：Frank Chen')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('140x120')  # 这里的乘是小x

#第一行
l_1 = tk.Label(window, text='自动填写', font=(16), height=1)
l_1.grid(column=1,row=1) 
#第二行
screening='negative'
def select_screening():
    global screening
    if (var1.get() == 1) :     # 如果选中第一个选项，未选中第二个选项
        screening='positive'
    elif (var1.get() == 2):
        screening='negative'
var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var1.set(2)
r1= tk.Radiobutton(text='positive', variable=var1, value=1,command=select_screening)
r1.grid(column=1, row=2)
r2= tk.Radiobutton(text='negative', variable=var1, value=2,command=select_screening)
r2.grid(column=1, row=3)

#
def auto_result():
    time.sleep(3)
    for i in range(3):
        pyautogui.typewrite('%s'%screening) 
        pyautogui.typewrite(['down'])

b_1= tk.Button(window, text='自动\n填写', font=('Arial', 12), height=2, command=auto_result)
b_1.grid(column=2,row=2)
window.mainloop()