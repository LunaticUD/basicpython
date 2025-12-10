# 生成器的本质就是迭代器
# 生成器的创建
# 1.通过生成器换数创建
# 2.通过生成器表达式来实现生成器
# 一般函数
# def func():
#     print(123456)
#     return "789"
# ret = func()
# print("得到的返回值是：",ret)
# 生成器函数
# def func():
#     print(123456)
#     yield "123456789"               # 关键在于yield,该函数就是一个生成器函数，且yield也具有返回值的效果
# ret = func()                        # 生成生成器
# print("得到的返回值是：",ret)       # <generator object func at 0x00000168A39C8970>获得的是一个生成器的地址
# r1 = ret.__next__()
# print("得到的返回值是：",r1)        # 通过__next__函数进行获取值
# r2 = ret.__next__()
# print("得到的返回值是：",r2)        # 没有值了会报错StopIteration，通过yield返回生成器函数的返回值
# 在一个生成器函数中可以有多个yield
# def func():
#     print(123456)
#     yield "123456789" 
#     print("www")
#     yield "23"
#     print("999")
#     yield "99"
#     print("888")
# ret = func()
# r1 = ret.__next__()
# print("得到返回值：",r1)
# r2 = ret.__next__()
# print("得到返回值：",r2)
# r3 = ret.__next__()
# print("得到返回值：",r3)
# r4 = ret.__next__()
# print("得到返回值：",r4)
# 生成器函数：
# 1。里面有yield
# 2。生成器在执行的过程其实就是在创建一个生成器出来
# 3。必须通过__next__函数来执行一段代码，到下一个yield结束
# 4。yield也有返回的意思，可以让一个函数分段执行
# 5。当后面没有yield函数时，再次执行会报错StopIteration

# 生成器最大的作用就是节省内存
# 常规函数
# def f():
#     lit = []
#     for i in range(1,101):
#         lit.append(f"{i}袋方便面") 
#     return lit

# r = f()
# print(r)
# 生成器函数
# 需要时获取一袋方便面
# def f():
#     for i in range(1,101):
#         yield f"{i}袋方便面"

# r = f()
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())

# 需要时获取5袋方便面
# def f():
#     lit = []                            # 🌽准备一个列表，开始执行
#     for i in range(1,101):           
#         lit.append(f"{i}袋方便面")
#         if len(lit)==5:    
#             yield lit                   # 🌽到此结束
#             lit = []                    # 再次准备一个列表进行循环
# r = f()
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())

# # send()函数
# def func():
#     print(1)
#     a = yield "111"
#     print(2,a)
#     b = yield "222"
#     print(3,b)
#     yield "333"

# g = func()
# print(g.__next__())                     # 第一次运行必须用__next__函数,才能用send函数
# print(g.send("qqq"))                    # 程序正常执行,发送"qqq"给a,而a原来为None
# print(g.__next__())

# 生成器推导式
# l = (i for i in range(10))
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# 拿空生成器的对象
# 1.for循环
# 生成器->迭代器->可迭代对象->for循环
# for i in l:
#     print(i)
# 可以用list tuple set拿空数据
# print(list(l))
# l = (i for i in range(10))
# print(tuple(l))
# l = (i for i in range(10))
# print(set(l))

# 生成器函数
# def func():
#     print(111)
#     yield "222"
# g = func()
# g1 = (i for i in g)
# g2 = (i for i in g1)
# print(list(g))
# print(list(g1))
# print(list(g2))

# yield from
# def d():
#     l1 = ["1","2","3"]
#     l2 = ["a","b","c"]
#     # for i in l1:
#         # yield i
#     yield from l1
#     # for x in l2:
#         # yield x
#     yield from l2           # 等价与注释,是将列表中的每一个元素返回,两个yield from 并不会发生交替
# g = d()
# print(list(g))


