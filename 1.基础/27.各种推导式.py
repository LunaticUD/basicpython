# 列表推导式
# 常规产生列表
# lt = []
# for i in range(100):
#     lt.append(i)
# print(lt)
# 列表的推导式:[结果 for循环 if条件]
# a = [ a for a in range(10) ]
# b = [ b**2 for b in range(10) ]
# c = [ c for c in range(10) if c % 2]
# d = [ "好X%s"%d for d in range(10) ]
# print(a)
# print(b)
# print(c)
# print(d)
# 字典的推导式:{key:value for循环 if条件}
# lt = ["nn","mm","uu"]
# l = {i:lt[i] for i in range(len(lt))}
# print(l)
# 集合的推导式:{key for循环 if条件}
# lt = ["1","2","2","3"]
# s = {i for i in range(10)}
# g = {i for i in lt}
# print(s)
# print(g)
# 元组没有推导式,是不可变形,不能增删改
# 而以下获得的是一个生成器,为生成器 
# lt = (i for i in range(10))
# print(lt)
