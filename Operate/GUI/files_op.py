# -*- coding:utf-8 -*-
import shutil
import os

def remove_file(old_path, new_path):
    # print(old_path)
    # print(new_path)
    filelist = os.listdir(old_path)      #列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
    # print(filelist)
    for file in filelist:
        f = old_path + '/' + file
        photh_list = os.listdir(f)
        for each in photh_list:
            src = os.path.join(f, each)
            dst = os.path.join(new_path, each)
            # print('src:', src)                 # 原文件路径下的文件
            # print('dst:', dst)                 # 移动到新的路径下的文件
            shutil.move(src, dst)

if __name__ == '__main__':
    old_path = '../Apple iPad\Internal Storage\DCIM'          # 原文件夹路径
    new_path = 'C:\Data\ipad照片'      # 新文件夹路径
    remove_file(old_path, new_path)

