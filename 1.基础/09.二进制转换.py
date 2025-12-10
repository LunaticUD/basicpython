# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:17:42 2022

@author: 32230
"""

# 进制转换
# 其他转换成十进制
def convert_ten(i,a):
    result = int(i,a)
    print(result)
# 十进制转换为二进制
def convert_two(i):
    if a=='10':
        print(str(bin(int(i))).lstrip('0b'))
    else:
        j = int(i,a)
        print(str(bin(int(j))).lstrip('0b'))
# 十进制转换为八进制
def convert_eight(i):
    if a=='10':
        print((oct(i)).lstrip('0o'))
    else:
        j = int(i,a)
        print((oct(j)).lstrip('0o'))
# 十进制转换为十六进制
def convert_sixteen(i):
    if a=='10':
        print(str(hex(i)).lstrip('0x'))
    else:
        j = int(i,a)
        print(str(hex(j)).lstrip('0x'))
    
a = int(input("请输入进制数："))
b = input("请输入要转成进制数：")
i = input("请输入值：")
try:
    if b=='10':
        convert_ten(i,a)
    elif b=='2':
        convert_two(i)
    elif b=='8':
        convert_eight(i)
    else:
        convert_sixteen(i)
except:
    print("输入有误")

