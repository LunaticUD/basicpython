# 递归函数
# 一个函数在内部调用自身本身，即为递归函数
# 递归的关键且相同点是都在一个函数内存在两个return
# 斐波那契数列
require_use = int(input("请输入你要获得第几位数（纯数字）："))
def Run(n):
    '''
    递归:调用自身
    ① 明确你这个函数要做什么
    ② 寻找递归结束的条件
    ③ 找出函数的等价关系式
    '''
    if n == 1 or n == 2:        # 递归结束条件
        return 1                                           # --->   递归
    return Run(n-1) + Run(n-2)  # 函数的等价关系式           #  --->    关键
result = Run(require_use)
print(result)
# 汉诺塔
def hanoi(n,a,b,c):
    if n==1:
        print(a,"-->",c)
    else:
        hanoi(n-1,a,c,b)
        print(a,"-->",c)
        hanoi(n-1,b,a,c)
hanoi(8,"a","b","c")

# 详细

# [1,1,2,3,5,8,13,21,...]
# 第n位数是多少
require_use = int(input("请输入你要获得第几位数（纯数字）："))
# f(n) = f(n-1) + f(n-2)

# 解法一


# def Run(n):
#     '''
#     n    :为位数
#     Run():求斐波那契数列
#     公式         数                       n          结果
#     a = 1       # 1                     # 1         # 1
#     b = a       # 1                     # 2         # 1
#     c = b + a   # 1 + 1                 # 3         # 2
#     d = c + b   # 1 + 1 + 1             # 4         # 3
#     e = d + c   # 1 + 1 + 1 + 1 + 1     # 5         # 5
#     '''
#     i = 3
#     dicts = {1: 1, 2: 1}
#     if n == 1 or n == 2:
#         print(1)
#     else:
#         while i <= n:
#             dicts[i] = dicts[i-1] + dicts[i-2]
#             i += 1
#         print(dicts[n])


# Run(require_use)

# 解法二

def Run(n):
    '''
    递归:调用自身
    ① 明确你这个函数要做什么
    ② 寻找递归结束的条件
    ③ 找出函数的等价关系式
    '''
    if n == 1 or n == 2:        # 递归结束条件
        return 1                                           # --->   递归
    return Run(n-1) + Run(n-2)  # 函数的等价关系式           #  --->    关键


result = Run(require_use)
print(result)
