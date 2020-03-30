# import pandas as pd
# import numpy as np
# a = ['one','two','three']
# b = [1,2,3]
# english_column = pd.Series(a, name='english')
# number_column = pd.Series(b, name='number')
# predictions = pd.concat([english_column, number_column], axis=1)
# print(predictions)
# #another way to handle
# save = pd.DataFrame({'english':a,'number':b})
# print(save)
#
#
# list_l = [[11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]
# date_range = pd.date_range(start="20180701", periods=3)
# df = pd.DataFrame(list_l, index=date_range,
#                   columns=['a', 'b', 'c', 'd', 'e'])
# print(df)
#
# l1 = [11,'', 12, 13, 14, 15]
# l2 = [21, 22,'', 23, 24, 25]
# l3 = [31, 32, 33, 34,'', 35]
#
# batchData = pd.DataFrame({'a':l1,'b':l2,'c':l3})
# batchData.to_csv('C:\\Users\\chenhuai\\Desktop\\result\\test.csv',mode='a',index=0,header=0)

# def factorial(n) :
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# a=factorial(4)
#
# print(a)
#
# def factorial(n) :
#     if n == 1:
#         return 1
#     return n + factorial(n - 1)
#
# a=factorial(4)
#
# print(a)

b = {'1':'','2':'1','3':'','4':'1,2,3','5':'','6':'4','7':'6'}

def aaa(c,i=0):
    print(c)
    if c=='':
        print('wu')
        i += 1
    else:
        d = b['%s'%c].split(',')
        print(d)
        for each in d:
            i += 1
            # print(i)
            aaa(each,i)

aaa(3)