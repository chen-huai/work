# -*- coding:utf-8 -*-
import os;
import re

def reset():
    i = 0
    path = r"C:\Users\chen-fr\Desktop\result\\";
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files);  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue;
        filename = os.path.splitext(files)[0];  # 文件名
        filetype = os.path.splitext(files)[1];  # 文件扩展名
        filePath = path + filename + filetype
        alter(filePath)


def alter(file):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    with open(file, "r+", encoding="utf-8") as f1:
        for line in f1:
            old_str = re.findall('\d{1,2}.\d{1,4}E.*\d{1,4} ug/l',line)
            #print(old_str)
            if old_str !=[]:
                mid_str = old_str[0].split(' ')[0].replace('E','e')
                #exp_str = mid_str[1].split(' ')[0]
                print(mid_str)
                new_str = "{:.2f}".format(mid_str)
                print(new_str)
            print(line)

            #line = line.replace(old_str, new_str)
            #f2.write(line)
    #os.remove(file)
    #os.rename("%s.bak" % file, file)


reset()
