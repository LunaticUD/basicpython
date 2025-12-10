#demo1404:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 10, 20) #在-1到10的区间内生成20个数据
y1 = 100* x + 10  #直线 y1
y2 = 2**x   #曲线 y2
plt.plot(x, y1, 'r+',color="red", linewidth=1.0, linestyle="-", label='line1')
# 绘制颜色为蓝色、宽度为 1 像素的连续直线 y1，数据点为+号形式
plt.plot(x, y2, 'bo', color="#800080", linewidth=2.0, linestyle="--", label='line2')
# 绘制颜色为紫色、宽度为 2 像素的不连续曲线 y2,数据点为圆点形式
plt.xlim(-2,11) # 设置横轴的最大最小值
plt.legend(["y=100x+10","y=2^x"],loc='upper left') #在左上角显示图例
plt.show()