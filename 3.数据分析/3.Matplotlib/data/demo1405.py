import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots()

x = np.linspace(-2*np.pi, 2*np.pi, 256)  #生成从-π到π的256个数据
cos,sin = np.cos(x), np.sin(x) #分别计算x的cos和sin函数值
ax.set_xticks( [-2*np.pi, -1*np.pi, 0, np.pi, 2*np.pi]) #设置x轴的刻度

plt.plot(x, cos, color="blue", linewidth=2, linestyle="-", label="cos")
#画出cos曲线，颜色为蓝色，线宽为2，连续线
plt.plot(x, sin, color="red",  linewidth=2, linestyle="--", label="sin")
#画出sin曲线，颜色为红色，线宽为2，间断线

ax.spines["right"].set_visible(False)#隐藏右边框
ax.spines["top"].set_visible(False)#隐藏上边框
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) #设置下边框到y轴0的位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0)) #设置左边框到x轴0的位置

plt.legend(loc='lower left')
plt.show()