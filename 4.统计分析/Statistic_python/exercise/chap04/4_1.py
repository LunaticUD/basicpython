import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
os.chdir('exercise/chap04')
da = pd.read_csv('exercise4_1.csv')
mean = da['网购金额'].mean()
sd = da['网购金额'].std()
R = da['网购金额'].max()-da['网购金额'].min()
IQR = da['网购金额'].quantile(q=0.75)-da['网购金额'].quantile(q=0.25)
print(f"平均数：{mean}\n标准差：{round(sd,4)}\n极差：{R}\n四分位差：{IQR}")
print(da['网购金额'].quantile(q=[0.1,0.25,0.5,0.75,0.9],interpolation='linear'))
skew = da['网购金额'].skew()
kurt = da['网购金额'].kurt()
print(f"偏度系数：{round(skew,4)}\n峰度系数：{round(kurt,4)}")
z = stats.zscore(da['网购金额'],ddof=1)
x = da['网购金额']
T = (x-min(x))/(max(x)-min(x))
plt.subplots(1,2,figsize=(8,6))
plt.subplot(121)
sns.kdeplot(x=z,bw_method=0.5)
plt.title('标准化分数')
plt.subplot(122)
sns.kdeplot(x=T,bw_method=0.5)
plt.title('极差标准化')
plt.tight_layout()
plt.show()