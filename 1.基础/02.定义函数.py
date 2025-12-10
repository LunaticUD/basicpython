# 定义函数
# # 使用def语句
# def my_abs(x):
#     if x>=0:
#         n = x
#     else:
#         n = -x
#     return n
# print(my_abs(-1))
# # 空函数
# def nop():
#     pass
# # 参数检查
# # print(my_abs(1,2))
# # print(my_abs('a'))
# # 数据类型检查用isinstance
# # 错误类型返回为raise
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('请正确输入')
#     elif x>=0:
#         n = x
#     else:
#         n = -x
#     return n
# print(my_abs(-1))
# print(my_abs(0))
# print(my_abs(1))
# print(my_abs('1'))
# 返回多个值
import math
def pythagorean(a,b):
    c = math.sqrt(a**2+b**2)
    ac = math.degrees(math.acos(a/c))
    bc = math.degrees(math.acos(b/c))
    return c,ac,bc
print('据勾股定理得c边长为%d,a与c边的夹角为%.1f,b与c的夹角为%.1f'%(pythagorean(4,4)))