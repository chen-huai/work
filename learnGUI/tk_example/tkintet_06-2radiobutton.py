"""
@Author : 行初心
@Date   : 18-10-1
@Blog   : www.cnblogs.com/xingchuxin
@Gitee  : gitee.com/zhichengjiu
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *



root = Tk()

group1 = LabelFrame(root, text='服器部', padx=5, pady=5)
group1.pack(side=RIGHT, padx=10, pady=10)

v = IntVar()
v.set(3)

rb1_group1 = Radiobutton(group1, text='锦', variable=v, value=1, indicatoron=False)
rb1_group1.pack(fill=X)

rb2_group1 = Radiobutton(group1, text='绢', variable=v, value=2, indicatoron=False)
rb2_group1.pack(fill=X)

rb3_group1 = Radiobutton(group1, text='帛', variable=v, value=3, indicatoron=False)
rb3_group1.pack(fill=X)

group2 = LabelFrame(root, text='果部', padx=5, pady=5)
group2.pack(side=LEFT, padx=10, pady=10)

v2 = IntVar()
v2.set(2)

rb1_group2 = Radiobutton(group2, text='李', variable=v2, value=1, indicatoron=False)
rb1_group2.pack(fill=X)

rb2_group2 = Radiobutton(group2, text='杏', variable=v2, value=2, indicatoron=False)
rb2_group2.pack(fill=X)

rb3_group2 = Radiobutton(group2, text='梅', variable=v2, value=3, indicatoron=False)
rb3_group2.pack(fill=X)

mainloop()


