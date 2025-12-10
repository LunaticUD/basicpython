# # random()函数的用法
# # 1.random.random()
# # 用于生成一个0到1的随机浮点数：0<=n<1.0
import random
print('random.random()', random.random())
# # 2.random.uniform(a,b)
# # 用于生成一个指定范围内的随机浮点数，两个参数其中一个是上限，一个是下限，如果a>b,则生成的随机数n：b<=n<=a.
# # 如果a<b,则a<=n<=b
print('random.uniform1', random.uniform(1, 10))
print('random.uniform2', random.uniform(20, 10))
# # 3.random.randint(a,b)
# # 用于生成一个指定范围内的整数。其中a为上限，b为下限，生成的随机数n:a<=n<=b
print('random.randint',random.randint(1,10))
print('random.randint',random.randint(10,10))
# # 4.random.randrange([start],stop[,step])
# # 从指定范围内，按指定基数递增的集合中获取一个随机数。
print('random.randrange', random.randrange(1,100,10))
# # 5.random.choice(sequence)
# # sequence表示一个有序类型，在python中不是一种特定的类型，而是泛指一系列的类型，list，tuple，字符串都属于sequence
print('random.choice',random.choice('I love python'))
print('random.choice',random.choice(['I ','love ','python']))
print('random.choice',random.choice(('I ','love ','python')))
print('random.choice',random.choice({'1':'I ','2':'love ','3':'python'}))
# # 6.random.shuffle(x[,random])
# # 用于将一个列表中的元素打乱
li=[1,2,3,4,5,6]
random.shuffle(li)
print(li)
# # 7.random.sample(sequence,k)
# # 从指定序列中获取指定长度的片断。sample函数不会修改原有序列
list=[1,2,3,4,5,6,7,8,9,0]
s=random.sample(list,5)
print(s)
print(list)
