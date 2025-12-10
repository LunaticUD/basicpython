#demo1401:
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5,6,7,8,9,10])   #创建一个numpy数组x
y=x*x*x     #创建一个numpy数组，内容为x中数据的平方值
plt.bar(x,y)  #调用bar函数画直方图
plt.show()   #显示图像
