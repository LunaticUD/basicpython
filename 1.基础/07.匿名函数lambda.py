# 匿名函数用一句话编写简单的函数
# def d(n):
#     return n**2
# ret = d(8)
# print(ret)
# 语法格式:lambda表达式:lambda 参数 : 返回值
# fn = lambda n:n**2         # <function <lambda> at 0x000001F845DEEF70>把创建好的lambda函数赋值于fn
# # print(ret)
# ret = fn(8)
# print(ret)
fn1 = lambda m,n:m+n
fn2 = lambda m,n:(m+n,m*n)
a = fn1(8,8)
b = fn2(8,8)
print(a,b)

# 函数的参数可以有多个，之间用逗号隔开
# 匿名函数不管有多么复杂都写一行，逻辑结束后直接返回数据
# 返回值与正常函数的值一样，可以是多种类型
