# # 格式化
# # %式
# print('hello,%s,%d,%.1f'%('dragon',6,6.6))
# # format式
# print("dragon{}".format(',hello'))
# # '%.2f'% num <=> '{0:.2f}'.format(num)
# # f-string式
# r = 2
# PI= 3.14159265359
# s = PI*r**2
# print(f'the area of a circle is {r} or {s}')

# 详细

# 格式化字符串
# #TODO: 1.使用‘%’操作符
# # '%[-][+][0][m][.n]格式字符’%exp
# # -:可选参数，用于指定左对齐，正数前面无符号，负数前面加负号
# # +：可选参数，用于指定右对齐，正数前面加正号，负数前面加负号
# # 0：可选参数，表示右对齐，正数前面无符号，负数前面加负号，用0填充空白处(一般与m参数一起使用)
# # m:可选参数，表示占有的宽度
# # 。n：可选参数，表示小数点后保留的位数
# # 格式字符：用于指定类型
# # %s字符串（采用str（）方法显示）%c单个字符%d或者%i十进制整数%x十六进制正数%f或者%F浮点数%r字符串（采用repr（）方法显示）%o八进制整数%e指数基底写为e%E指数基底写为E%%字符%
# # exp：要转换的项，如果要指定的项有多个，需要通过元组的形式进行指定,不可以是列表
# a = '编号 %03d %s http://www.%s.com'
# b = (1, '百度', 'baidu')
# c = (2, '搜狗', 'sougo')
# d = (3, '谷歌', 'google')
# print(a % b+'\n'+a % c+'\n'+a % d)
#TODO: 2.format()方法格式化字符串
# str.format(args)
# str创建模板，用{}和：实现
# args用于要指定的项
# {[index][:[[fill]align][sign][#][width][.precision][type]]}
# index设置格式的对象在参数列表中的索引位置，如果省略，值的先后循序自动分配
# fill填充字符
# align<左对齐>右对齐=只对数字有效为右对齐^居中
# sign指定有无符号数，+正加正负加负-正不加负加负‘ ’正加空格负加负
# #进制加0b/0o/0x
# width宽度
# .precision保留的小数位数
# type指定类型
# a = '编号:\n {:->9d}\n {:->9d}\n {:->9d}\n {:->9d}\n'.format(1, 2, 3, 4+8)
# print(a)
def fun(a, b):
    m = '{:s} http://www.{:s}.com'
    x = m.format(a, b)
    # b = a.format(1, '百度', 'baidu')
    # c = a.format(2, '搜狗', 'sougo')
    # d = a.format(3, '谷歌', 'google')
    return x


i = input()
j = input()
print(fun(i, j))

# print('{:->6,}'.format(1234))
#TODO:嵌套格式化
a = input("请输入填充符号：")
s = "PYTHON"
print("{:{}^30}".format(s,a))
# 居中格式化
a = input("请输入填充符号：")
s = 'python'
print(s.center(30,a))