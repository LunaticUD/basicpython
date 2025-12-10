# dict
# 键值对存储
# 一、获取key值
d = {'arch':2,'debian':1,'opensuse':3}
print(d['arch'])
# # 添加元素,且key只能是一个,且不能没有
# d['ubuntu'] = 4
# print(d['ubuntu'])
# d['ubuntu'] = 5
# print(d['ubuntu'])
# # print(d['gentoo']) # 会报错
# print('gentoo' in d)
# # 二、获取key值
# print(d.get('arch'))
# print(d.get('gentoo'))
# print(d.get('gentoo','NO'))
# 查找、插入速度快于list，且与key无关
# 要占用大量内存
# key值不可变，且不能用list
# key = [1,2,3]
# d[key] = 'a list'
# print(d[key])
# dict.get(key[, value]) 
dict1 = {1: 2, 0: 3, 4: 1, 9: 6, 5: 14, 3: 8, 2: 1} #定义一个字典
dict1_sorted_keys = sorted(dict1.keys())
# 使用位置参数，将dict1.keys()传给iterable，按照dict1的键进行升序排列
print(dict1_sorted_keys)
dict1_sorted_items = sorted(dict1.items())
print(dict1_sorted_items)
dict1_sorted_items1 = sorted(dict1.items(),key = lambda x:x[0],reverse = True)
print(dict1_sorted_items1)
# 字典的最小值
print(min({'c':5,'b':6,'a':7}))
# 类型
d={(1,2):1,(3,4):3}
# d={'python':1,[tea,cat]:2}        # ❌
# d={1:as,2:sf}                     # ❌
# d={[1,2]:1,[3,4]:3}               # ❌
# d.get()函数
dit = {'name':'carlo','age':7,'sex':'girl'}
print(dit.get('name'))
print(dit.get('horby'))
print(dit.get('name',100))
print(dit.get('horby',100))
print(dit)
# 例
d={}
for i in range(26):
	d[chr(i+ord("A"))]=chr((i+13)%26+ord("A"))
for c in "Python":
	print(d.get(c,c),end="")
print(d)