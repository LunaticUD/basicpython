# Random库
import random

# random.random()函数，#TODO:返回一个[0.0,1.0]之间#TODO:的伪随机小数#TODO:
print(random.random())
# random.uniform(a,b)函数，#TODO:生成一个[a,b]之间#TODO:的随机小数#TODO:（包含a,b）
print(random.uniform(1, 10))
# random.randint(a,b)函数,#TODO:生成一个[a,b]之间#TODO:的随机整数#TODO:（包含a,b）
print(random.randint(1, 10))
# random.choice(seq)函数,可以#TODO:从序列类型中随机返回一个元素#TODO:
print(random.choice("I Love You!"))
# random.shuffle(seq)函数可以#TODO:将一个列表中的元素打乱#TODO:，随即排列#TODO:
l1 = list(range(20))
print(l1)
random.shuffle(l1)
print(l1)
# random.sample(pop,k)函数从#TODO:pop序列类型中随机选取k个元素#TODO:，以列表类型返回
print(random.sample(l1, 6))
# random.randrange(start,stop[,step])函数可以#TODO:生成一个[start,end)之间以step为步长的随机整数#TODO:。
print(random.randrange(1, 10, 2))
# random.seed(a=None) #TODO:初始化随机数种子，默认为当前系统时间#TODO:
random.seed(1)
print(random.random())
