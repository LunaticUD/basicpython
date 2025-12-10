import numpy as np

print('均值为0，标准差为1，标准正态分布随机数10个：' + '\n',
      np.random.standard_normal(10))
print('均值为100，标准差为20，正态分布随机数10个：' + '\n',
      np.random.normal(loc=100, scale=20, size=10))
print('1~1000均匀分布随机数10个：' + '\n',
      np.random.uniform(low=1, high=1000, size=10))
