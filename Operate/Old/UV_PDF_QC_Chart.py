# _*_ coding: utf-8 _*_

import easygui as g
import datetime
import os
import os.path
import codecs, sys
import win32com.client as win32com
import tkinter
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import win32timezone
import time
import re

now = time.strftime('%Y')

print("开始")


def HCHO():
    root = tkinter.Tk()
    path = tkinter.filedialog.askopenfilenames(initialdir="Z:/Data/%s/66-01-2016-051 UV-Vis (60)" % now,
                                               title="Select files", filetypes=[("pdf file", "*.pdf")])
    root.destroy()

    excel = win32com.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    excel.Application.DisplayAlerts = True

    workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), 'Z:/QC Chart/%s/QC Chart_HCHO_CARY60.xlsx' % now))
    maxcolumn = 8
    while excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(3, maxcolumn).Value is not None:
        maxcolumn += 1
    k = 0
    for each1 in path:
        p = r'%s' % each1
        pdf = PdfFileReader(open(p, 'rb'))
        total_page_number = pdf.getNumPages()
        page_number = 0

        while page_number < total_page_number:

            pageobj = pdf.getPage(page_number)
            text = pageobj.extractText()

            a = text.split('\n')
            b = a[1].split(' ')
            date = b[0]
            print(date)
            lenth = len(a)

            count = 0

            while count < lenth:
                if ('QC' in a[count]) and ('*' not in a[count]):
                    if ('/' not in a[count + 1]) and (float(a[count + 1]) > 0.5):
                        excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(2, maxcolumn + k).Value = date
                        excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(2, maxcolumn + k).NumberFormat = "m/d/yyyy"
                        excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(3, maxcolumn + k).Value = a[count]
                        excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(4, maxcolumn + k).Value = float(a[count + 1])
                        k += 1

                count += 1
            page_number += 1


def Cr():
    root = tkinter.Tk()
    path = tkinter.filedialog.askopenfilenames(initialdir="Z:/Data/%s/66-01-2013-011 UV-Vis (100)" % now,
                                               title="Select files", filetypes=[("pdf file", "*.pdf")])
    root.destroy()

    excel = win32com.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    excel.Application.DisplayAlerts = True
    workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), r'Z:/QC Chart/%s/QC Chart_Cr_CARY100.xlsx' % now))
    maxcolumn = 8
    while excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(3, maxcolumn).Value is not None:
        maxcolumn += 1

    k = 0
    for each1 in path:
        print(each1)
        p = r'%s' % each1
        pdf = PdfFileReader(open(p, 'rb'))
        total_page_number = pdf.getNumPages()
        page_number = 1
        while page_number < total_page_number:
            pageobj = pdf.getPage(page_number)
            text = pageobj.extractText()
            a = text.split(' ')
            for each in a:
                if (('QC' in each) or ('qc' in each)) and ('*' not in each) and ('/' not in each):
                    content1 = each.split(' ')

                    content2 = []
                    for each in content1:
                        if each != '':
                            content2.append(each)
                            content1 = ''.join(content2)
                            content2 = content1.split('QC')
                            qc_value = re.findall("\d+\.+\d+\d+\d", content2[1])
                            content2 += qc_value

                            excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(2, maxcolumn + k).Value = a[0]
                            excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(2, maxcolumn + k).NumberFormat = "m/d/yyyy"
                            excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(3, maxcolumn + k).Value = 'QC'
                            excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(4, maxcolumn + k).Value = float(content2[2])
                            excel.Sheets("TC_XMN_CHM_F_Q.67E").Cells(4, maxcolumn + k).NumberFormat = "0.000"
                            k += 1

            page_number += 1


option = g.ccbox('which test item', title='UV QC data input', choices=('Cr', 'HCHO'))
if option == 1:
    Cr()
else:
    HCHO()

g.msgbox('结束 ')

