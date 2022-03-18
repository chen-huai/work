#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import tkinter
import pickle
# Excel 调用相关库
import openpyxl
import xlwings

from win32com.client import Dispatch
import easygui as g
import os
import os.path
import win32com.client as win32com
import win32clipboard as wc
import time
import datetime
import calendar
import pyautogui
from tkinter import *
import tkinter.messagebox
from tkinter import scrolledtext

def getCopyText():
    wc.OpenClipboard()
    copytext = wc.GetClipboardData()
    wc.CloseClipboard()
    return copytext

def click_1():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    # 第2步，给窗口的可视化起名字
    window.title('作者：Irene Wang')
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('421x265')  # 这里的乘是小x
    # 第一行
    l_1 = tk.Label(window, text='Run POC', font=(16), height=1)
    l_1.grid(column=2, row=1)
    # 第二行
    var1 = IntVar(window)  # 定义var1和var2整型变量用来存放选择行为返回值

    def select_method():
        global method
        if (var1.get() == 1):  # 如果选中第一个选项，未选中第二个选项
            method = 'T run'
            print(method)
        elif (var1.get() == 2):
            method = 'P run'
            print(method)

    r1 = tk.Radiobutton(window, text='T run', variable=var1, value=1, command=select_method)
    r1.grid(column=1, row=2)
    r2 = tk.Radiobutton(window, text='P run', variable=var1, value=2, command=select_method)
    r2.grid(column=3, row=2)

    l_2 = tk.Label(window, text='Fiscal Year', font=(14))
    l_2.grid(column=1, row=3)
    l_3 = tk.Label(window, text='Period', font=(14))
    l_3.grid(column=2, row=3)
    l_4 = tk.Label(window, text='Company code', font=(14))
    l_4.grid(column=3, row=3)

    # 第四行
    e_1 = tk.StringVar(window)
    e_1_name = tk.Entry(window, textvariable=e_1, width=10, font=(14))
    e_1_name.grid(column=1, row=4)
    e_1_name.focus()

    e_2 = tk.StringVar(window)
    e_2_name = tk.Entry(window, textvariable=e_2, width=10, font=(14))
    e_2_name.grid(column=2, row=4)
    e_3 = tk.StringVar(window)
    e_3_name = tk.Entry(window, textvariable=e_3, width=10, font=(14))
    e_3_name.grid(column=3, row=4)

    # 第五行
    l_10 = tk.Label(window, text='请再次\n确认信息\n是否填全', font=(1))
    l_10.grid(column=2, row=8)

    def auto_result():
        time.sleep(3)
        pyautogui.typewrite("/nsa38")
        pyautogui.typewrite(['enter'])
        time.sleep(5)
        pyautogui.typewrite("ZCO_ABGR_POC_RUN            ")
        pyautogui.typewrite(['tab'] * 11)
        pyautogui.typewrite(['enter'])
        time.sleep(5)
        if method == 'T run':
            pyautogui.typewrite('T')
        elif method == 'P run':
            pyautogui.typewrite('P')
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite('%s' % e_1.get())
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite('%s' % e_2.get())
        pyautogui.typewrite(['tab'] * 3)
        if method == 'T run':
            pyautogui.typewrite(['Space'])
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite('%s' % e_3.get())
        pyautogui.typewrite(['F9'])
        time.sleep(15)
        pyautogui.typewrite(['tab'] * 5)

        pyautogui.typewrite(['enter'])
        time.sleep(10)

        pyautogui.typewrite(['tab'] * 4)
        pyautogui.typewrite(['enter'])
        time.sleep(3)
        pyautogui.typewrite(['tab'] * 2)
        pyautogui.typewrite(['enter'])

    b_1 = tk.Button(window, text='自动\nRun PoC', font=('Arial', 12), height=2, command=auto_result)
    b_1.grid(column=3, row=8)

    window.mainloop()
def click_2():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('操作界面，作者：Controlling CoE Team')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('535x320')  # 这里的乘是小x
    window.resizable(0, 0)
    # 第一行
    l_1 = tk.Label(window, text='Open PoC Order', font=('Arial', 16, 'bold'), width=30, height=2)
    l_1.place(x=0, y=0)

    # 第一列
    t_1 = tk.scrolledtext.ScrolledText(window, width=30, height=15)
    t_1.insert('end', '显示导入的excel信息：\n')
    t_1.place(x=5, y=50)

    # 第二列，第一行
    l_2 = tk.Label(window, text='请输入起始编号：', font=('Arial', 14), height=2)
    l_2.place(x=300, y=30)

    var_usr_name = tk.StringVar(window)
    var_usr_name.set(1)
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, width=17, font=('Arial', 14))
    entry_usr_name.place(x=300, y=80)
    entry_usr_name.focus()

    def select_file1():
        global path, list, id_number, order_status, order_operation
        path = tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES/SVHC' % now_1,
                                                   filetypes=[("file", "*.xls*")])
        # 文件位置有什么特定需求？
        list = []
        id_number = []
        order_status = []
        order_operation = []
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        excel = win32com.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        excel.Application.DisplayAlerts = True
        workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % path))
        row = 2
        x = 100
        # t_1.delete(1.0, tkinter.END)
        # t_1.insert('end','显示输入的编号信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.see(tk.END)
        window.update()

        while excel.Sheets('Order_List').Cells(x, 1).Value is not None:
            x += 1
        for i in range(x - 1):
            result = excel.Sheets("Order_List").Cells(row, 2).Value
            id_no = excel.Sheets("Order_List").Cells(row, 1).Value
            status = excel.Sheets("Order_List").Cells(row, 5).Value
            operation = excel.Sheets("Order_List").Cells(row, 6).Value
            list.append(result)
            id_number.append(id_no)
            order_status.append(status)
            order_operation.append(operation)

            row += 1
        window.update()

    b_1 = tk.Button(window, text='选择order list', font=('Arial', 12), width=20, height=1, command=select_file1)
    b_1.place(x=300, y=125)

    def get_data1():
        v.set(2)
        t_1.delete(1.0, tkinter.END)
        ##清除调用者text中的内容，防止下一次判断的时候重复打印上次的内容
        ##0.0代表的是小标为第0行的第0个元素，后面的tkinter.END表示末尾，
        t_1.insert('end', '显示导入的excel信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.insert('end', '即将输入的起始编号：\n%s \n' % int(var_usr_name.get()))
        t_1.see(tk.END)

        window.update()
        fill_sample_number = int(var_usr_name.get())
        m = id_number.index(fill_sample_number)
        t_1.insert('end', '编号%d\norder No：%d\nstaus: %s\nOperation: %s\n' % (
        id_number[m], list[m], order_status[m], order_operation[m]))

        time.sleep(5)
        len_id_number = set(id_number)
        window.update()
        for n in range(len(len_id_number) - 1):
            window.update()
            if v.get() == 1:
                t_1.insert('end', '============================\n')
                break
            else:
                print(m + 1, len(list), len(id_number), n, len(len_id_number), range(len(len_id_number) - 1))
                if m + 1 < len(list):
                    while id_number[m] == id_number[m + 1]:
                        if str(list[m]) == '-2146826273':  # 没懂这串数字
                            m += 1
                        else:
                            if str(list[m + 1]) == '-2146826273':
                                list[m + 1] = list[m]
                            else:
                                list[m + 1] = min(list[m], list[m + 1])
                        m += 1
                    if list[m] < 0:
                        list[m] = 0

                    # 开始进行open order 操作，从VA02的界面开始
                    pyautogui.typewrite('%d' % list[m], 0)  # 用%d来转换成整数
                    pyautogui.typewrite(['Enter'])
                    time.sleep(0.5)
                    #pyautogui.typewrite(['tab'])  # 考虑到consider the subsequent documents的情况，似乎finished order都有？
                    pyautogui.typewrite(['Enter'])
                    time.sleep(0.5)
                    pyautogui.typewrite(['Enter'])
                    time.sleep(0.5)

                    time.sleep(0.4)
                    pyautogui.keyDown('alt')
                    pyautogui.typewrite('G')
                    pyautogui.typewrite('H')
                    pyautogui.typewrite('S')
                    pyautogui.keyUp('alt')
                    pyautogui.typewrite(['tab'] * 3)
                    pyautogui.typewrite(['Enter'])
                    pyautogui.typewrite(['tab'] * 2)

                    print(len(order_status[m]))

                    if len(order_status[m]) >= 8:
                        method1 = 'SREG+ABGS'
                    else:
                        method1 = 'SREG'

                    if method1 == 'SREG':
                        pyautogui.typewrite(['Space'])
                    elif method1 == 'SREG+ABGS':  # 需要判断ABGS是否有勾上
                        pyautogui.typewrite(['Space'])
                        pyautogui.typewrite(['Down'])
                        pyautogui.typewrite(['Space'])
                    pyautogui.typewrite(['F3'])
                    pyautogui.typewrite(['tab'] * 2)
                    pyautogui.typewrite(['Right'])
                    pyautogui.typewrite(['Enter'])
                    pyautogui.typewrite(['tab'] * 4)
                    print('%s' % order_operation[m])
                    if order_operation[m] == "Open":
                        pyautogui.typewrite(['Left'])
                    else:
                        pyautogui.typewrite(['Right'])

                    # pyautogui.typewrite(['tab']*9)
                    # pyautogui.typewrite(['Enter'])
                    pyautogui.hotkey('ctrl', 's')
                    time.sleep(0.5)

                    t_1.insert('end', '%d 已经保存\n' % (list[m]))
                    #  t_1.insert('end', '结果：%d\n' % list[m])
                    window.update()
                    # pyautogui.typewrite(['Enter'])
                    t_1.insert('end', '\n即将开始\n编号%d\norder No：%d\nstaus: %s\nOperation: %s\n' % (
                    id_number[m + 1], list[m + 1], order_status[m + 1], order_operation[m + 1]))
                    #    t_1.insert('end', '即将输入的起始编号：%d\n' % id_number[m + 1])
                    t_1.see(tk.END)
                    window.update()
                    time.sleep(3)
                else:
                    # pyautogui.typewrite(['right'] * 6)
                    # pyautogui.typewrite('%s' % id_number[m], 0.0000000001)
                    t_1.insert('end', '============================\n')
                m += 1

    b_2 = tk.Button(window, text='确认开始', font=('Arial', 12), width=20, height=1, command=get_data1)
    b_2.place(x=300, y=195)

    # 第二列，第五行
    v = tk.IntVar(window)
    v.set(2)
    rb1 = tk.Radiobutton(window, text='停止', font=('Arial', 12), variable=v, value=1, indicatoron=False, width=20, height=1)
    rb1.place(x=300, y=245)
    #rb2 = tk.Radiobutton(window, text='继续', variable=v, value=2, indicatoron=False, width=10, height=2)
    #rb2.place(x=430, y=245)
    window.update
    window.mainloop()
def click_3():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('操作界面，作者：Controlling CoE Team')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('535x320')  # 这里的乘是小x
    window.resizable(0, 0)
    # 第一行
    l_1 = tk.Label(window, text='Download Allevo', font=('Arial', 16, 'bold'), width=30, height=2)
    l_1.place(x=0, y=0)

    # 第一列
    t_1 = tk.scrolledtext.ScrolledText(window, width=30, height=15)
    t_1.insert('end', '显示下载Allevo信息：\n')
    t_1.place(x=5, y=50)

    # 第二列，第一行
    l_2 = tk.Label(window, text='请输入起始profit center：', font=('Arial', 14), height=2)
    l_2.place(x=300, y=30)

    var_usr_name = tk.StringVar(window)
    var_usr_name.set(41601330)
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, width=17, font=('Arial', 14))
    entry_usr_name.place(x=300, y=80)
    entry_usr_name.focus()

    def select_file2():
        global path, id_number, pc_number, pc_no, Save_Address
        path = tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES/SVHC' % now_1,
                                                   filetypes=[("file", "*.xls*")])
        # 文件位置有什么特定需求？

        id_number = []
        pc_number = []

        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        excel = win32com.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        excel.Application.DisplayAlerts = True
        workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % path))
        row = 2
        x = 1000
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.see(tk.END)
        window.update()

        # while excel.Sheets('PC_List').Cells(x, 1).Value is not None:
        #    x += 1
        Save_Address = excel.Sheets("PC_List").Cells(1, 3).Value
        for i in range(x - 1):
            #        result = excel.Sheets("PC_List").Cells(row, 2).Value
            pc_no = excel.Sheets("PC_List").Cells(row, 1).Value
            id_no = excel.Sheets("PC_List").Cells(row, 1).Value

            pc_number.append(pc_no)
            id_number.append(id_no)

            row += 1
        window.update()

    b_1 = tk.Button(window, text='选择Profit Center list', font=('Arial', 12), width=20, height=1, command=select_file2)
    b_1.place(x=300, y=125)

    def get_data2():
        v.set(2)
        t_1.delete(1.0, tkinter.END)
        ##清除调用者text中的内容，防止下一次判断的时候重复打印上次的内容
        ##0.0代表的是小标为第0行的第0个元素，后面的tkinter.END表示末尾，
        t_1.insert('end', '显示导入的excel信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.insert('end', '即将Download的PC：\n%s \n' % int(var_usr_name.get()))
        t_1.see(tk.END)

        window.update()
        fill_sample_number = int(var_usr_name.get())  # fill_sample_number = 41601330
        m = id_number.index(fill_sample_number)  # fill_sample_number 在ID_NUMBER中的位置m=0
        t_1.insert('end', '开始profit center:%d\n' % (pc_number[m]))

        time.sleep(5)
        len_id_number = set(id_number)  # 去除id_number重复项目
        window.update()
        for n in range(len(len_id_number) - 1):
            window.update()
            if v.get() == 1:
                t_1.insert('end', '============================\n')
                break
            else:
                print(m + 1, len(pc_number), len(id_number), n, len(len_id_number), range(len(len_id_number) - 1),
                      Save_Address)
                if m + 1 < len(pc_number):
                    '''
                    while id_number[m] == id_number[m + 1]:
                        if str(pc_number[m]) == '-2146826273':   #没懂这串数字
                            m += 1
                        else:
                            if str(pc_number[m + 1]) == '-2146826273':
                                pc_number[m + 1] = pc_number[m]
                            else:
                                pc_number[m + 1] = min(pc_number[m], pc_number[m + 1])
                        m += 1
                    if pc_number[m] < 0:
                       pc_number[m] = 0
                #开始进行Download Allevo 操作，从/n/kern/ippks的界面开始，并已选好了planning template
                         '''
                    pyautogui.typewrite('%d' % pc_number[m], 0)  # 用%d来转换成整数
                    pyautogui.typewrite(['Tab'] * 3)
                    pyautogui.typewrite(['Enter'])
                    time.sleep(110)  # 打开allevo file，等待150秒'''
                    pyautogui.typewrite(['F12'])  # 用F12调出保存界面，不确定会不会因为不同电脑快捷键设置不同
                    time.sleep(5)
                    pyautogui.typewrite('%s\%d.xlsm' % (Save_Address, pc_number[m]), 0)

                    time.sleep(5)
                    pyautogui.typewrite(['Enter'])
                    time.sleep(15)  # 保存操作，等30秒

                    pyautogui.keyDown('alt')
                    time.sleep(3)
                    pyautogui.typewrite('A')
                    time.sleep(3)
                    pyautogui.keyUp('alt')
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)

                    pyautogui.typewrite(['Tab']* 4)
                    time.sleep(3)
                    pyautogui.typewrite(['Enter'])
                    time.sleep(3)
                    pyautogui.typewrite(['Tab'])
                    time.sleep(3)
                    pyautogui.typewrite(['Enter'])

                    time.sleep(15)
                    t_1.insert('end', '%d 已经保存\n' % (pc_number[m]))

                    window.update()

                    t_1.insert('end', '\n即将开始\nPC %d\n' % (pc_number[m + 1]))

                    t_1.see(tk.END)
                    window.update()

                else:

                    t_1.insert('end', '============================\n')
                m += 1

    b_2 = tk.Button(window, text='确认开始', font=('Arial', 12), width=20, height=1, command=get_data2)
    b_2.place(x=300, y=195)

    # 第二列，第五行
    v = tk.IntVar(window)
    v.set(2)
    rb1 = tk.Radiobutton(window, text='停止', font=('Arial', 12), variable=v, value=1, indicatoron=False, width=20, height=1)
    rb1.place(x=300, y=245)
    #rb2 = tk.Radiobutton(window, text='继续', variable=v, value=2, indicatoron=False, width=10, height=2)
    #rb2.place(x=430, y=245)
    window.update
    window.mainloop()
def click_4():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('操作界面，作者：Controlling CoE Team')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('535x320')  # 这里的乘是小x
    window.resizable(0, 0)
    # 第一行
    l_1 = tk.Label(window, text='Addtional Data B', font=('Arial', 16, 'bold'), width=30, height=2)
    l_1.place(x=0, y=0)

    # 第一列
    t_1 = tk.scrolledtext.ScrolledText(window, width=30, height=15)
    t_1.insert('end', '显示导入的excel信息：\n')
    t_1.place(x=5, y=50)

    # 第二列，第一行
    l_2 = tk.Label(window, text='请输入起始编号：', font=('Arial', 14), height=2)
    l_2.place(x=300, y=30)

    var_usr_name = tk.StringVar(window)
    var_usr_name.set(1)
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, width=17, font=('Arial', 14))
    entry_usr_name.place(x=300, y=80)
    entry_usr_name.focus()

    def select_file1():
        global path, list, id_number, order_status, order_operation
        path = tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES/SVHC' % now_1,
                                                   filetypes=[("file", "*.xls*")])
        # 文件位置有什么特定需求？
        list = []
        id_number = []
        order_status = []
        order_operation = []
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        excel = win32com.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        excel.Application.DisplayAlerts = True
        workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % path))
        row = 2
        x = 100
        # t_1.delete(1.0, tkinter.END)
        # t_1.insert('end','显示输入的编号信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.see(tk.END)
        window.update()

        while excel.Sheets('Order_List').Cells(x, 1).Value is not None:
            x += 1
        for i in range(x - 1):
            result = excel.Sheets("Order_List").Cells(row, 2).Value
            id_no = excel.Sheets("Order_List").Cells(row, 1).Value
            status = excel.Sheets("Order_List").Cells(row, 5).Value
            operation = excel.Sheets("Order_List").Cells(row, 6).Value
            list.append(result)
            id_number.append(id_no)
            order_status.append(status)
            order_operation.append(operation)

            row += 1
        window.update()

    b_1 = tk.Button(window, text='选择order list', font=('Arial', 12), width=20, height=1, command=select_file1)
    b_1.place(x=300, y=125)

    def get_data1():
        global currency_rate, order_value, addtional_datab_value
        v.set(2)
        t_1.delete(1.0, tkinter.END)
        ##清除调用者text中的内容，防止下一次判断的时候重复打印上次的内容
        ##0.0代表的是小标为第0行的第0个元素，后面的tkinter.END表示末尾，
        t_1.insert('end', '显示导入的excel信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.insert('end', '即将输入的起始编号：\n%s \n' % int(var_usr_name.get()))
        t_1.see(tk.END)

        window.update()
        fill_sample_number = int(var_usr_name.get())
        m = id_number.index(fill_sample_number)

        t_1.insert('end', '编号%d\norder No：%d\nstaus: %s\nOperation: %s\n' % (
        id_number[m], list[m], order_status[m], order_operation[m]))

        time.sleep(5)
        len_id_number = set(id_number)
        window.update()

        for n in range(len(len_id_number) - 1):
            window.update()
            if v.get() == 1:
                t_1.insert('end', '============================\n')
                break
            else:
                print(m + 1, len(list), len(id_number), n, len(len_id_number), range(len(len_id_number) - 1))
                if m + 1 < len(list):
                    while id_number[m] == id_number[m + 1]:
                        if str(list[m]) == '-2146826273':  # 没懂这串数字
                            m += 1
                        else:
                            if str(list[m + 1]) == '-2146826273':
                                list[m + 1] = list[m]
                            else:
                                list[m + 1] = min(list[m], list[m + 1])
                        m += 1
                    if list[m] < 0:
                        list[m] = 0

                    # 开始进行open order 操作，从VA02的界面开始
                    pyautogui.typewrite('%d' % list[m], 0)  # 用%d来转换成整数
                    pyautogui.typewrite(['Enter'])
                    pyautogui.typewrite(['tab'])  # 考虑到consider the subsequent documents的情况，似乎finished order都有？
                    pyautogui.typewrite(['Enter'])

                    time.sleep(0.6)


                    #copy order value
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('ctrl')
                    pyautogui.typewrite(['Up'] * 100)
                    pyautogui.typewrite(['left'] * 1)
                    pyautogui.typewrite(['Up'] * 6)
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('ctrl')

                    pyautogui.typewrite(['right'] * 20)
                    pyautogui.keyDown('shift')
                    pyautogui.typewrite(['left'] * 20)
                    pyautogui.keyUp('shift')

                    pyautogui.hotkey('ctrl', 'c')
                    pyautogui.hotkey('ctrl', 'c')

                    order_value = getCopyText()
                    order_value = order_value.replace(" ", "")  #删除空白字符，包括：\n，\r，\t
                    order_value = order_value.replace(",", "")
                    print(order_value)
                    addtional_datab_value = round(float(order_value), 2)

                    if order_operation[m] == "Y":
                        # copy currency rate
                        pyautogui.keyDown('alt')
                        pyautogui.typewrite('G')
                        pyautogui.typewrite('H')
                        pyautogui.typewrite('A')
                        pyautogui.keyUp('alt')

                        pyautogui.keyDown('alt')
                        pyautogui.keyDown('ctrl')
                        pyautogui.typewrite(['Right']*13)
                        pyautogui.keyUp('alt')
                        pyautogui.keyUp('ctrl')

                        pyautogui.keyDown('shift')
                        pyautogui.typewrite(['Right'] * 10)
                        pyautogui.keyUp('shift')

                        pyautogui.hotkey('ctrl', 'c')
                        pyautogui.hotkey('ctrl', 'c')

                        currency_rate = getCopyText()
                        currency_rate = currency_rate.replace(" ", "")# 删除空白字符，包括：\n，\r，\t
                        currency_rate = currency_rate.replace(",", "")

                        print(currency_rate)

                        pyautogui.typewrite(['F3'])
                        addtional_datab_value = round(float(order_value) * float(currency_rate), 2)
                        '''
                        pyautogui.typewrite(['tab']*24)
                        pyautogui.typewrite(['Right'] * 4)
                        pyautogui.typewrite(['Enter'])
                        pyautogui.keyDown('alt')
                        pyautogui.keyDown('ctrl')
                        pyautogui.typewrite(['Up']*1000)
                        pyautogui.typewrite(['left'] * 1)
                        pyautogui.typewrite(['Up'] * 4)
                        pyautogui.keyUp('alt')
                        pyautogui.keyUp('ctrl')
    
                        pyautogui.keyDown('shift')
                        pyautogui.typewrite(['right'] * 20)
                        pyautogui.keyUp('shift')
    
                        pyautogui.hotkey('ctrl', 'c')
                        order_value = getCopyText()
                        order_value.replace(' ', '')
                        order_value.lstrip(' ')#删除空白字符，包括：\n，\r，\t
    
                        print(order_value)
                        '''
                        #计算和修改additional datab 金额

                    print(addtional_datab_value)

                    pyautogui.keyDown('alt')
                    pyautogui.typewrite('G')
                    pyautogui.typewrite('H')
                    pyautogui.typewrite('F')
                    pyautogui.typewrite('D')
                    pyautogui.keyUp('alt')
                    pyautogui.typewrite(['tab']*7)

                    addtional_datab_value=str(addtional_datab_value)
                    pyautogui.typewrite(addtional_datab_value)

                    pyautogui.hotkey('ctrl', 's')

                    time.sleep(1)

                    t_1.insert('end', '%d 已经保存\n' % (list[m]))
                    #  t_1.insert('end', '结果：%d\n' % list[m])
                    window.update()
                    # pyautogui.typewrite(['Enter'])
                    t_1.insert('end', '\n即将开始\n编号%d\norder No：%d\nstaus: %s\nOperation: %s\n' % (
                    id_number[m + 1], list[m + 1], order_status[m + 1], order_operation[m + 1]))
                    #    t_1.insert('end', '即将输入的起始编号：%d\n' % id_number[m + 1])
                    t_1.see(tk.END)
                    window.update()
                    # time.sleep(3)
                else:
                    # pyautogui.typewrite(['right'] * 6)
                    # pyautogui.typewrite('%s' % id_number[m], 0.0000000001)
                    t_1.insert('end', '============================\n')
                m += 1

    b_2 = tk.Button(window, text='确认开始', font=('Arial', 12), width=20, height=1, command=get_data1)
    b_2.place(x=300, y=195)

    # 第二列，第五行
    v = tk.IntVar(window)
    v.set(2)
    rb1 = tk.Radiobutton(window, text='停止', font=('Arial', 12), variable=v, value=1, indicatoron=False, width=20, height=1)
    rb1.place(x=300, y=245)
    #rb2 = tk.Radiobutton(window, text='继续', variable=v, value=2, indicatoron=False, width=10, height=2)
    #rb2.place(x=430, y=245)
    window.update
    window.mainloop()
def click_5():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('操作界面，作者：Controlling CoE Team')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('535x320')  # 这里的乘是小x
    window.resizable(0, 0)
    # 第一行
    l_1 = tk.Label(window, text='Download Allevo', font=('Arial', 16, 'bold'), width=30, height=2)
    l_1.place(x=0, y=0)

    # 第一列
    t_1 = tk.scrolledtext.ScrolledText(window, width=30, height=15)
    t_1.insert('end', '显示下载Allevo信息：\n')
    t_1.place(x=5, y=50)

    # 第二列，第一行
    l_2 = tk.Label(window, text='请输入起始profit center：', font=('Arial', 14), height=2)
    l_2.place(x=300, y=30)

    var_usr_name = tk.StringVar(window)
    var_usr_name.set(41601330)
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, width=17, font=('Arial', 14))
    entry_usr_name.place(x=300, y=80)
    entry_usr_name.focus()

    def select_file2():
        global path, id_number, pc_number, pc_no, Save_Address
        path = tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES/SVHC' % now_1,
                                                   filetypes=[("file", "*.xls*")])
        # 文件位置有什么特定需求？

        id_number = []
        pc_number = []

        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        excel = win32com.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        excel.Application.DisplayAlerts = True
        workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % path))
        row = 2
        x = 1000
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.see(tk.END)
        window.update()

        # while excel.Sheets('PC_List').Cells(x, 1).Value is not None:
        #    x += 1
        Save_Address = excel.Sheets("PC_List").Cells(1, 3).Value
        for i in range(x - 1):
            #        result = excel.Sheets("PC_List").Cells(row, 2).Value
            pc_no = excel.Sheets("PC_List").Cells(row, 1).Value
            id_no = excel.Sheets("PC_List").Cells(row, 1).Value

            pc_number.append(pc_no)
            id_number.append(id_no)

            row += 1
        window.update()

    b_1 = tk.Button(window, text='选择Profit Center list', font=('Arial', 12), width=20, height=1, command=select_file2)
    b_1.place(x=300, y=125)

    def get_data2():
        v.set(2)
        t_1.delete(1.0, tkinter.END)
        ##清除调用者text中的内容，防止下一次判断的时候重复打印上次的内容
        ##0.0代表的是小标为第0行的第0个元素，后面的tkinter.END表示末尾，
        t_1.insert('end', '显示导入的excel信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.insert('end', '即将Upload的PC：\n%s \n' % int(var_usr_name.get()))
        t_1.see(tk.END)

        window.update()
        fill_sample_number = int(var_usr_name.get())  # fill_sample_number = 41601330
        m = id_number.index(fill_sample_number)  # fill_sample_number 在ID_NUMBER中的位置m=0
        t_1.insert('end', '开始profit center:%d\n' % (pc_number[m]))

        time.sleep(5)
        len_id_number = set(id_number)  # 去除id_number重复项目
        window.update()
        for n in range(len(len_id_number) - 1):
            window.update()
            if v.get() == 1:
                t_1.insert('end', '============================\n')
                break
            else:
                print(m + 1, len(pc_number), len(id_number), n, len(len_id_number), range(len(len_id_number) - 1),
                      Save_Address)
                if m + 1 < len(pc_number):
                    '''
                    while id_number[m] == id_number[m + 1]:
                        if str(pc_number[m]) == '-2146826273':   #没懂这串数字
                            m += 1
                        else:
                            if str(pc_number[m + 1]) == '-2146826273':
                                pc_number[m + 1] = pc_number[m]
                            else:
                                pc_number[m + 1] = min(pc_number[m], pc_number[m + 1])
                        m += 1
                    if pc_number[m] < 0:
                       pc_number[m] = 0
                #开始进行Download Allevo 操作，从/n/kern/ippks的界面开始，并已选好了planning template
                         '''
                    pyautogui.typewrite('%d' % pc_number[m], 0)  # 用%d来转换成整数

                    pyautogui.typewrite(['Down'] * 1)
                    time.sleep(3)
                    pyautogui.typewrite(['Tab'] * 1)
                    time.sleep(3)
                    pyautogui.typewrite(['Tab'] * 2)
                    time.sleep(3)
                    pyautogui.typewrite(['Enter'])
                    time.sleep(10)  # 打开选择文件的界面，等待30秒'''
                    pyautogui.keyDown('alt')
                    time.sleep(3)
                    pyautogui.typewrite('N')
                    time.sleep(3)
                    pyautogui.keyUp('alt')
                    pyautogui.typewrite('%s\%d.xlsm' % (Save_Address, pc_number[m]), 0)
                    pyautogui.typewrite(['Tab'] * 2)
                    time.sleep(3)
                    pyautogui.typewrite(['Enter'])
                    time.sleep(50) # 打开allevo文件，等待150秒'''
                    pyautogui.keyDown('alt')
                    time.sleep(3)
                    pyautogui.typewrite('A')
                    time.sleep(3)
                    pyautogui.keyUp('alt')
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)
                    pyautogui.typewrite(['F7'])
                    time.sleep(3)
                    pyautogui.typewrite(['Enter'])
                    time.sleep(3)
                    pyautogui.keyDown('alt')
                    time.sleep(3)
                    pyautogui.typewrite('C')
                    time.sleep(3)
                    pyautogui.keyUp('alt') #用alt + C是因为有时候会跳出来debug界面，直接continue过去， 如果直接保存了，alt +C应该是不影响的
                    time.sleep(50)  # 保存allevo文件，等待150秒'''
                    pyautogui.keyDown('Tab')
                    time.sleep(3)
                    pyautogui.keyDown('Enter')
                    time.sleep(3)
                    pyautogui.keyDown('alt')
                    time.sleep(3)
                    pyautogui.typewrite('A')
                    time.sleep(3)
                    pyautogui.keyUp('alt')
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)
                    pyautogui.typewrite(['EsC'])
                    time.sleep(3)

                    pyautogui.typewrite(['F3'])
                    time.sleep(5)

                    pyautogui.typewrite(['Tab'])
                    time.sleep(5)
                    pyautogui.typewrite(['Enter'])

                    time.sleep(20)
                    t_1.insert('end', '%d 已经保存\n' % (pc_number[m]))

                    window.update()

                    t_1.insert('end', '\n即将开始\nPC %d\n' % (pc_number[m + 1]))

                    t_1.see(tk.END)
                    window.update()

                else:

                    t_1.insert('end', '============================\n')
                m += 1

    b_2 = tk.Button(window, text='确认开始', font=('Arial', 12), width=20, height=1, command=get_data2)
    b_2.place(x=300, y=195)

    # 第二列，第五行
    v = tk.IntVar(window)
    v.set(2)
    rb1 = tk.Radiobutton(window, text='停止', font=('Arial', 12), variable=v, value=1, indicatoron=False, width=20, height=1)
    rb1.place(x=300, y=245)
    #rb2 = tk.Radiobutton(window, text='继续', variable=v, value=2, indicatoron=False, width=10, height=2)
    #rb2.place(x=430, y=245)
    window.update
    window.mainloop()
def click_6():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('操作界面，作者：Controlling CoE Team')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('535x320')  # 这里的乘是小x
    window.resizable(0, 0)
    # 第一行
    l_1 = tk.Label(window, text='Open PoC Order', font=('Arial', 16, 'bold'), width=30, height=2)
    l_1.place(x=0, y=0)

    # 第一列
    t_1 = tk.scrolledtext.ScrolledText(window, width=30, height=15)
    t_1.insert('end', '显示导入的excel信息：\n')
    t_1.place(x=5, y=50)

    # 第二列，第一行
    l_2 = tk.Label(window, text='请输入起始编号：', font=('Arial', 14), height=2)
    l_2.place(x=300, y=30)

    var_usr_name = tk.StringVar(window)
    var_usr_name.set(1)
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, width=17, font=('Arial', 14))
    entry_usr_name.place(x=300, y=80)
    entry_usr_name.focus()

    def select_file1():
        global path, list, id_number, order_status, order_operation
        path = tkinter.filedialog.askopenfilenames(initialdir='Z:/Data/%s/66-01-2018-012 5110 ICP-OES/SVHC' % now_1,
                                                   filetypes=[("file", "*.xls*")])
        # 文件位置有什么特定需求？
        list = []
        id_number = []
        order_status = []
        order_operation = []
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        excel = win32com.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        excel.Application.DisplayAlerts = True
        workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), r'%s' % path))
        row = 2
        x = 100
        # t_1.delete(1.0, tkinter.END)
        # t_1.insert('end','显示输入的编号信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.see(tk.END)
        window.update()

        while excel.Sheets('Order_List').Cells(x, 1).Value is not None:
            x += 1
        for i in range(x - 1):
            result = excel.Sheets("Order_List").Cells(row, 2).Value
            id_no = excel.Sheets("Order_List").Cells(row, 1).Value
            status = excel.Sheets("Order_List").Cells(row, 5).Value
            operation = excel.Sheets("Order_List").Cells(row, 6).Value
            list.append(result)
            id_number.append(id_no)
            order_status.append(status)
            order_operation.append(operation)

            row += 1
        window.update()

    b_1 = tk.Button(window, text='选择order list', font=('Arial', 12), width=20, height=1, command=select_file1)
    b_1.place(x=300, y=125)

    def get_data1():
        global currency_rate, order_value, addtional_datab_value
        v.set(2)
        t_1.delete(1.0, tkinter.END)
        ##清除调用者text中的内容，防止下一次判断的时候重复打印上次的内容
        ##0.0代表的是小标为第0行的第0个元素，后面的tkinter.END表示末尾，
        t_1.insert('end', '显示导入的excel信息：\n')
        t_1.insert('end', '%s\n' % os.path.basename(os.path.realpath(path[0])))
        t_1.insert('end', '即将输入的起始编号：\n%s \n' % int(var_usr_name.get()))
        t_1.see(tk.END)

        window.update()
        fill_sample_number = int(var_usr_name.get())
        m = id_number.index(fill_sample_number)

        t_1.insert('end', '编号%d\norder No：%d\nstaus: %s\nOperation: %s\n' % (
            id_number[m], list[m], order_status[m], order_operation[m]))

        time.sleep(5)
        len_id_number = set(id_number)
        window.update()
        for n in range(len(len_id_number) - 1):
            window.update()
            if v.get() == 1:
                t_1.insert('end', '============================\n')
                break
            else:
                print(m + 1, len(list), len(id_number), n, len(len_id_number), range(len(len_id_number) - 1))
                if m + 1 < len(list):
                    while id_number[m] == id_number[m + 1]:
                        if str(list[m]) == '-2146826273':  # 没懂这串数字
                            m += 1
                        else:
                            if str(list[m + 1]) == '-2146826273':
                                list[m + 1] = list[m]
                            else:
                                list[m + 1] = min(list[m], list[m + 1])
                        m += 1
                    if list[m] < 0:
                        list[m] = 0

                    # 开始进行open order 操作，从VA02的界面开始
                    pyautogui.typewrite('%d' % list[m], 0)  # 用%d来转换成整数
                    pyautogui.typewrite(['Enter'])
                    pyautogui.typewrite(['tab'])  # 考虑到consider the subsequent documents的情况，似乎finished order都有？
                    pyautogui.typewrite(['Enter'])

                    time.sleep(0.4)

                    # copy order value
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('ctrl')
                    pyautogui.typewrite(['Up'] * 1000)
                    pyautogui.typewrite(['left'] * 1)
                    pyautogui.typewrite(['Up'] * 6)
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('ctrl')

                    pyautogui.typewrite(['right'] * 20)
                    pyautogui.keyDown('shift')
                    pyautogui.typewrite(['left'] * 20)
                    pyautogui.keyUp('shift')

                    pyautogui.hotkey('ctrl', 'c')
                    order_value = getCopyText()
                    order_value = order_value.replace(" ", "")  # 删除空白字符，包括：\n，\r，\t
                    order_value = order_value.replace(",", "")
                    print(order_value)
                    addtional_datab_value = round(float(order_value), 2)

                    if order_operation[m] == "Y":
                        # copy currency rate
                        pyautogui.keyDown('alt')
                        pyautogui.typewrite('G')
                        pyautogui.typewrite('H')
                        pyautogui.typewrite('A')
                        pyautogui.keyUp('alt')

                        pyautogui.keyDown('alt')
                        pyautogui.keyDown('ctrl')
                        pyautogui.typewrite(['Right'] * 13)
                        pyautogui.keyUp('alt')
                        pyautogui.keyUp('ctrl')

                        pyautogui.keyDown('shift')
                        pyautogui.typewrite(['Right'] * 10)
                        pyautogui.keyUp('shift')

                        pyautogui.hotkey('ctrl', 'c')
                        currency_rate = getCopyText()
                        currency_rate = currency_rate.replace(" ", "")  # 删除空白字符，包括：\n，\r，\t
                        print(currency_rate)
                        pyautogui.typewrite(['F3'])
                        addtional_datab_value = round(float(order_value) * float(currency_rate), 2)
                        '''
                        pyautogui.typewrite(['tab']*24)
                        pyautogui.typewrite(['Right'] * 4)
                        pyautogui.typewrite(['Enter'])
                        pyautogui.keyDown('alt')
                        pyautogui.keyDown('ctrl')
                        pyautogui.typewrite(['Up']*1000)
                        pyautogui.typewrite(['left'] * 1)
                        pyautogui.typewrite(['Up'] * 4)
                        pyautogui.keyUp('alt')
                        pyautogui.keyUp('ctrl')

                        pyautogui.keyDown('shift')
                        pyautogui.typewrite(['right'] * 20)
                        pyautogui.keyUp('shift')

                        pyautogui.hotkey('ctrl', 'c')
                        order_value = getCopyText()
                        order_value.replace(' ', '')
                        order_value.lstrip(' ')#删除空白字符，包括：\n，\r，\t

                        print(order_value)
                        '''
                        # 计算和修改additional datab 金额

                    print(addtional_datab_value)

                    pyautogui.keyDown('alt')
                    pyautogui.typewrite('G')
                    pyautogui.typewrite('H')
                    pyautogui.typewrite('F')
                    pyautogui.typewrite('D')
                    pyautogui.keyUp('alt')
                    pyautogui.typewrite(['tab'] * 7)

                    addtional_datab_value = str(addtional_datab_value)
                    pyautogui.typewrite(addtional_datab_value)

                    pyautogui.hotkey('ctrl', 's')

                    time.sleep(1)

                    t_1.insert('end', '%d 已经保存\n' % (list[m]))
                    #  t_1.insert('end', '结果：%d\n' % list[m])
                    window.update()
                    # pyautogui.typewrite(['Enter'])
                    t_1.insert('end', '\n即将开始\n编号%d\norder No：%d\nstaus: %s\nOperation: %s\n' % (
                        id_number[m + 1], list[m + 1], order_status[m + 1], order_operation[m + 1]))
                    #    t_1.insert('end', '即将输入的起始编号：%d\n' % id_number[m + 1])
                    t_1.see(tk.END)
                    window.update()
                    # time.sleep(3)
                else:
                    # pyautogui.typewrite(['right'] * 6)
                    # pyautogui.typewrite('%s' % id_number[m], 0.0000000001)
                    t_1.insert('end', '============================\n')
                m += 1

    b_2 = tk.Button(window, text='确认开始', font=('Arial', 12), width=20, height=1, command=get_data1)
    b_2.place(x=300, y=195)

    # 第二列，第五行
    v = tk.IntVar(window)
    v.set(2)
    rb1 = tk.Radiobutton(window, text='停止', font=('Arial', 12), variable=v, value=1, indicatoron=False, width=20,
                         height=1)
    rb1.place(x=300, y=245)
    # rb2 = tk.Radiobutton(window, text='继续', variable=v, value=2, indicatoron=False, width=10, height=2)
    # rb2.place(x=430, y=245)
    window.update
    window.mainloop()

now_1 = str(time.strftime('%Y'))
root = Tk()
root.title("Controlling package")
root.geometry('170x180')
# 是x 不是*

'''
l1 = Label(root, text="xls名：")
l1.pack() #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()
xls = Entry(root, textvariable = xls_text)
xls_text.set(" ")
xls.pack()
'''

button1=Button(root,text='Run_PoC',width=20,font=('GB2312',12),background='Tan',command=click_1)
button1.grid(row=2,column=0,sticky=W)
button2=Button(root,text='Open_Order',width=20,font=('GB2312',12),background='Tan',command=click_2)
button2.grid(row=3,column=0,sticky=W)
button3=Button(root,text='Download_allevo',width=20,font=('GB2312',12),background='Tan',command=click_3)
button3.grid(row=4,column=0,sticky=W)
button4=Button(root,text='Additional dataB',width=20,font=('GB2312',12),background='Tan',command=click_4)
button4.grid(row=5,column=0,sticky=W)
button5=Button(root,text='Upload_allevo',width=20,font=('GB2312',12),background='Tan',command=click_5)
button5.grid(row=6,column=0,sticky=W)
button6=Button(root,text='...',width=20,font=('GB2312',12),background='Tan',command=click_6)
button6.grid(row=7,column=0,sticky=W)

root.mainloop()












