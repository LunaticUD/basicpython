#demo1401-1:
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background') #设置图像风格
fig,ax=plt.subplots()
ax.set_title("square numbers")
x=np.array([1,2,3,4,5,6,7,8,9,10]) #创建一个numpy数组x
#x=np.array([-25,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11]) #创建一个numpy数组x
y=x*x    #创建一个numpy数组，内容为x中数据的平方值
#plt.bar(x,y)
plt.bar(x,y,color='r') #bar的颜色改为红色
for a,b in zip(x,y): #在直方图上显示数字
    plt.text(a,b+0.2,'%d'%b,ha = 'center',va = 'bottom',fontsize=20)
plt.show()
