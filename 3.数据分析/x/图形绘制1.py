import numpy as np
import matplotlib.pyplot as plt

## TOP 1
plt.style.use('classic')
fig,ax = plt.subplots()
# print(plt.style.available)
ax.set_title('$ y = e^{x} $')
x = np.array([1,2,3,4,5,6,7,8,9,10])
# 初级
# plt.bar(x,np.exp(x))
# 加一级
plt.bar(x,np.exp(x),color='g')
for a,b in zip(x,np.exp(x)):
  plt.text(a,b+0.2,'%d'%b,ha='center',va='bottom',fontsize=8)
plt.show()

## TOP 2
# plt.style.use('ggplot')
# fig,ax = plt.subplots()
# ax.set_title
