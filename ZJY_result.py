# -*- coding:utf-8 -*-
import os
import time
import re
import tkinter
from tkinter import filedialog
address=os.path.abspath('.')+'\\'
now = time.strftime('%Y%m%d')
def reset():
    i = 0
    path=tkinter.filedialog.askdirectory()+'/'
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        i = i + 1
        oldDir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(oldDir):  # 如果是文件夹则跳过
            continue
        fileName = os.path.splitext(files)[0]  # 文件名
        fileType = os.path.splitext(files)[1]  # 文件扩展名
        filePath = path + fileName + fileType
        folder = os.path.exists(address+now)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(address+now)  # makedirs 创建文件时如果路径不存在会创建这个路径
        filePath2 = address + now + '\\' + fileName + fileType
        print(1,filePath2)
        alter(filePath,filePath2)
def alter(file,file2):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param oldStr: 需要替换的字符串
    :param newStr: 替换的字符串
    :return: None
    """
    with open(file, "r", encoding="utf-8") as f1,open('%s.bak'%file2, "w", encoding="utf-8") as f2:
        for line in f1:
            oldStr = re.findall("\d{1,2}.\d{1,4}E.*\d{1,4} ug/l",line)
            print(line)
            print(oldStr)
            if oldStr !=[]:
                newStr = str(float(oldStr[0].split(' ')[0])) + ' ' + 'ug/l'
                print(newStr)
                line = line.replace(oldStr[0],newStr)
            f2.write(line)
    os.rename("%s.bak" %file2,file2)
reset()
