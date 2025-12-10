# 函数
# 直接调用
# 抽象化记忆
# 调用函数
a = abs(int(input('输入值：')))
print(a)
# 调用函数abs()将输入的数值转换为正数
b = max(input('输入值：'))
print(b)
# 调用函数max()将输入的所有数字选出最大的哪一个
# 数据类型的转换
# int()将所有的数转化为整数
print(type(int('121')))
# float()将所有的数转化为浮点数
print(type(float('121')))
# bool()将所有的数转化为布尔值
print(type(bool('121')))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量
a = int
i = a(input('xxx:'))
print(type(i))
