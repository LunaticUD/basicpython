# 数据类型
# 整数
print(0,1,100,-1,-1000,0xff00,"...")
# 浮点数
print(0.1,3.14,1.2e-5,"...")
# 字符串
print('a'+'\n'+'b'+'I m\' ok',)
print("""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
""")
# 布尔值
print(True+False,True,False)
print(True and False,True or False,True|False,not True,not False)
# 空值
print(None)
# 变量
a = 1
b = 2
print(a+b)
a = a + b
print(a+b)
c = '1'
d = True and False
print(type(c),type(d))
m = 5
n = 'Note!'
n = m
print(m)
# 常量
PI = 3.14159265359
print(PI,"\n","but","PI依旧是个变量",PI*2)
# 整除
print(10//3)
# 取余
print(10%3)
print("......")