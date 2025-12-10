BasePath = 'C:/Users/86166/Desktop/20190708/files'
#文件路径
import csv
import numpy as np
import matplotlib.pyplot as plt
Semester1 = []
Semester2 = []
plt.rcParams['font.sans-serif'] = ['SimHei']
fig,ax = plt.subplots()
ax.set_title('10位同学两个学期排名的对比')

with open(BasePath+'\\data1403.csv','r') as csvfile:
    f_csv = csv.reader(csvfile)
    for row in f_csv:
        Semester1.append(int(row[0]))
        Semester2.append(int(row[1]))

x = np.arange(1,11)#生成横轴数据
plt.bar(x,Semester1,0.3,alpha = 0.5,color = 'b')
plt.bar(x+0.3,Semester2,0.3,alpha = 0.5,color = 'r')


plt.grid(True,linestyle = '--',alpha = 0.8)
for a,b in zip(x,Semester1):
    plt.text(a,b+0.2,'%d'%b,ha = 'center',va = 'bottom',fontsize = 10)
for a,b in zip(x,Semester2):
    plt.text(a+0.3,b+0.2,'%d'%b,ha = 'center',va = 'bottom',fontsize = 10)

plt.show()

