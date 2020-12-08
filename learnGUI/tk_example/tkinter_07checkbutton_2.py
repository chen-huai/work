#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
 
window=tk.Tk()
window.title('checkbutton')
window.geometry('400x400')
 
 
#定义label用于显示
l=tk.Label(window,
            bg='red',
            width=40,height=2,
            text='u have not chosen anything yet')
l.pack()
 
def print_selection():
    if (op_mark[0].get()==1)&(op_mark[1].get()==1):
        l.config(text='你怎么两个人通吃啊！')
    elif(op_mark[0].get()==1)&(op_mark[1].get()==0):
        l.config(text='啊哈！我也喜欢成成！')
    elif(op_mark[0].get()==0)&(op_mark[1].get()==1):
        l.config(text='谁让你喜欢冉冉的，成成才能喜欢冉冉！')
    else:
        l.config(text='快选啊~我还等着你呢、')
    print(op_mark[0].get())
 
ops=['成成','冉冉']
op_mark=[tk.IntVar(),tk.IntVar()]

#这里注意onvalue和offvalue不能改名字，只能用这两个名字！我就被坑了。。
for i in range(len(ops)):
    cb=tk.Checkbutton(window,
                   text=ops[i],
                   variable=op_mark[i],
                   offvalue=0,
                   command=print_selection)
    cb.pack()
 
#下面的是没用for做的。
# def print_selection():
#     if (var1.get()==1)&(var2.get()==1):
#         l.config(text='你怎么两个人通吃啊！')
#     elif(var1.get()==1)&(var2.get()==0):
#         l.config(text='啊哈！我也喜欢成成！')
#     elif(var1.get()==0)&(var2.get()==1):
#         l.config(text='谁让你喜欢冉冉的，成成才能喜欢冉冉！')
#     else:
#         l.config(text='快选啊~我还等着你呢、')
# ops=['成成','冉冉']
 
# var1=tk.IntVar()
# var2=tk.IntVar()
# cb1=tk.Checkbutton(window,
#                 text=ops[0],
#                 variable=var1,#选定或不选定存放在var1这个变量里面。
#                 onvalue=1,#如果选定了，那么var1的值就是1
#                 offvalue=0,#如果没有选定，那var1的值就是0
#                 command=print_selection)
# cb1.pack()
# cb2=tk.Checkbutton(window,
#                 text=ops[1],
#                 variable=var2,#选定或不选定存放在var2这个变量里面。
#                 onvalue=1,#如果选定了，那么var2的值就是1
#                 offvalue=0,#如果没有选定，那var2的值就是0
#                 command=print_selection)
# cb2.pack()
 
tk.mainloop()
