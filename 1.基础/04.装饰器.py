# 装饰器：可以在不改变原有基础上，给函数前面或者后面添加新的功能
# 装饰器的应用
# 装饰器雏形
# 语法糖
# def wrapper(fn):
#     def inner():
#         print("改变插件以前")
#         fn()
#         print("改变插件以后")
#         pass
#     return inner
# @wrapper          # 相当于a = wrapper(a)  这里是整个装饰器的灵魂所在
# def a():
#     print("我是a")
#     pass
# a()
# 装饰器有参数
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         print("程序执行以前")
#         fn(*args,**kwargs)
#         print("程序执行以后")
#         pass
#     return inner

# @wrapper
# def a(user,password):
    # print(f"登录帐号为{user}，密码为{password}")
#     pass
# a("admin",123456)       # 这里执行的是inner函数，而inner函数没有值，要加入*args,**kwargs,也保证了传入或多或少的参数
# 目标函数带有返回值
# def weapper(fn):
#     def inner(*args,**kwargs):
#         print("在执行操作之前")
#         ret = fn(*args,**kwargs)        # 获得返回值给ret
#         print("在执行操作之后")
#         return ret                      # 将返回值ret返回ret
#     return inner 

# @weapper
# def a(users,password):                  # 此时函数执行的是inner()函数
#     print(f"登录账号为{users}，密码为{password}")
#     return "胜利！"                     # 目标函数具有返回值
# aw = a("admin",123456)                  # 将返回值赋值给aw
# print("我获得了",aw)

# 通用装饰器,写法
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         """在执行操作之前"""
#         ret = fn(*args,**kwargs)
#         """在执行操作之后"""
#         return ret
#     return inner

# @wrapper        
# def target(xxx,xxx):
#     """执行操做"""
#     return xxxx
#     pass

# target(xxx,xxx)
# print("xxxx",xxxx)

# 高阶装饰器
# 同一个函数被多个装饰器装饰
def wrapper1(fn):
    def inner(*args,**kwargs):
        print("执行操作以前1")
        ret = fn(*args,**kwargs)
        print("执行操作以后1")
        return ret
    return inner

def wrapper2(fn):
    def inner(*args,**kwargs):
        print("执行操作以前2")
        ret = fn(*args,**kwargs)
        print("执行操作以后2")
        return ret
    return inner

def wrapper3(fn):
    def inner(*args,**kwargs):
        print("执行操作以前3")
        ret = fn(*args,**kwargs)
        print("执行操作以后3")
        return ret
    return inner

@wrapper1
@wrapper2
@wrapper3               # 按就进原则分析
def a():
    print("word")
    pass
a()

# 带有参数的装饰器
# game = input("请输入你要玩得游戏：")
# b = input("请输入你要用的游戏外挂：")
# def gua(b):
#     def wrapper(fn):
#         def inner(*args,**kwargs):
#             print(f"开启{b}外挂")
#             ret = fn(*args,**kwargs)
#             print(f"结束{b}外挂")
#             return ret
#         return inner
#     return wrapper
# @gua(b)         # 先进行@之后的函数调用，再进行函数的装饰
# def a(game):
#     print(f"玩{game}")
#     pass

# a(game)
