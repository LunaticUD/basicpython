# 函数的参数
# 位置参数
def power(x,n):     # 位置参数
    return x**n
print(power(6,2))
# 默认参数
def power(x,n=2):   # 默认参数
    return x**n
print(power(6))

def l(l=[]):
    l.append('end')
    return l
print(l())      # --> ['end']
print(l())      # --> ['end', 'end']    # 故默认参数必须指向不变对象
# 可变参数
# 传入的参数个数是可变的
def calc(nu):
    sum = 0
    for n in nu:
        sum = sum + n*n
    return sum
print(calc([1,2,3]))
# 再次简化
def calc1(*nu):
    sum = 0
    for n in nu:
        sum = sum + n*n
    return sum
print(calc1(1,2,3))
# # 相比
# print(calc())   # 传入的nu不可为多个值或空值
# print(calc1())  # 传入的nu可以是多个值也可以是空值
# 但是当列表已经存在时
num = [1,2,3]
print(calc1(*num))
# <==>
print(calc1(num[0],num[1],num[2]))

# 关键词参数
# 允许传入0或任意多个含参数名的参数，且会自动组装一个dict
def per(name,age,**kw):
    print('\n',name,'\n',age,'\n',kw)
per('arch',30,city='us',histry=100)
a = {'city':'us','histry':'100'}
per('arch',30,city=a['city'],histry=a['histry'])
per('arch',30,**a)

# 命名关键字参数
# 用户传入的**kw是无限制的
def per(name,age,*,city='北京',histry):    # 限制传入的关键字参数为city与histry
    print(name,age,city,histry)         # 命名关键字参数也可以有默认值
per('opensuse',100,city='german',histry=100)
# per('opensuse',100,city='german')   # 没有histry参数会被判读为位置参数而报错，
# 故在限制关键字参数时要用*来分隔开来

# 参数之间
# 可以组合使用，但是顺序是一定的为
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
def per(*args,**kw):
    print('\n',args,'\n',kw)
per('arch',30,city='us',histry=100)