# list
lit = ['1','a','2',2]
print(lit,'\n',
    '列表长度为：',len(lit),'\n',
    '其中索引0为',lit[0],'\n',
    '其中索引-1为',lit[-1],'\n')
# -->可变序列
# 追加
lit.append('+2')
print(lit)
# 插入
lit.insert(1,'|3')
print(lit)
lit.insert(0,'|')
print(lit)
# 删除末尾
lit.pop()
print(lit)
# 删除指定
lit.pop(1)
print(lit)
# 替换
lit[0] = '>4'
print(lit)
# list内可以接受不同的数据类型
lit1 = ['123',123,True,['1',False],{1:'2'},(1,2)]
print(lit1,'......')
# lit1是嵌套的
print(lit1[3][1],'长度为',len(lit1))
# list也可以是空值
lit2 = []
print(lit2,'长度为',len(lit2))
# reverse() 函数：反向序列元素
lit3 = [1,3,8,9,'a']
lit3.reverse()
print(lit3)

# 注意
# 而list是可变对象
a = [1,9,6,8,5]
a.sort()
print(a)
# str是不变对象
b = 'ABCD'
c = b.replace('A','s')
print('未更改前：',b+'\n'+'更改后：',c)

# 调用函数是x='abcd'，只要x不为空，函数f()会被不断调用
L = 'abcd'
def f(x,result=['a','b','c','d']):
    if x:
        result.remove(x[-1])
        f(x[:-1])
    return result
print(f(L))