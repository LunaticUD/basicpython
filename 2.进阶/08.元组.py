# tuple
# -->不可变序列
tup = ('123',123,[1,2,3],{2})
print(tup,'\n',
    '长度为',len(tup),'\n',
    '索引0为',tup[0],'\n',
    '索引-1为',tup[-1])
# 空tuple
tup1 = ()
print(tup1,'长度为',len(tup1))
# 定义一个只有1个元素的tuple
tup2 = (1)
# 只有1个元素的tuple
tup3 = (1,)
print(tup2,tup3)
# tuple嵌套
print(tup[2][1])
# tuple的更改
print(tup)
tup[2][1] = 0
# tup[1] = 0 #-->变得是tuple中的list，改变tuple会报错
print(tup)