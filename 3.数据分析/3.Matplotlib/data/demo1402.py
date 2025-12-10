import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('dark_background') #设置图像风格
fig,ax=plt.subplots()
'''
ax.set_title("square numbers")
x=np.array([1,2,3,4,5,6,7,8,9,10]) #创建一个numpy数组x
y=x*x                              #创建一个numpy数组，内容为x中数据的平方值

plt.bar(x,y,color='r')
for a,b in zip(x,y): #在直方图上显示数字
    plt.text(a,b+0.2,'%d'%b,ha = 'center',va = 'bottom',fontsize=10)
plt.show()
'''
BasePath='c:\\code' #cvs文件的保存路径
import csv
scores=[] #创建一个列表对象
with open(BasePath+'\\data1402.csv', 'r') as csvfile:
    f_csv = csv.reader(csvfile) #读入文件
    for row in f_csv: #将每一行的数据保存到scores中
        scores.append(float(row[0]))

def count_elements(scores): #定义转换函数，统计每个分数值对应多少人数
    scorescount = {}  #定义一个字典对象
    for i in scores:
        scorescount[int(i)] = scorescount.get(int(i), 0) + 1 #累加每个分数值的人数
    return scorescount

counted = count_elements(scores)
print(counted)
plt.axis([50,100,0,30]) # 设置x轴和y轴的最小和最大值
plt.bar(counted.keys(),counted.values(),0.5,alpha=0.5,color='b')
# 绘制直方图，第三个参数表示直方图的宽度，alpha为透明度,color为颜色
plt.show()

