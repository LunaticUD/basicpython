import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
os.chdir('exercise/chap04')
da = pd.read_csv('exercise4_2.csv')

m_A = da['方法A']
m_B = da['方法B']
m_C = da['方法C']
m_A_skew = m_A.skew()
m_A_kurt = m_A.kurt()
m_B_skew = m_B.skew()
m_B_kurt = m_B.kurt()
m_C_skew = m_C.skew()
m_C_kurt = m_C.kurt()
print(pd.DataFrame({'方法A':{'偏度系数':m_A_skew,'峰度系数':m_A_kurt},
                    '方法B':{'偏度系数':m_B_skew,'峰度系数':m_B_kurt},
                    '方法C':{'偏度系数':m_C_skew,'峰度系数':m_C_kurt}}))
def zt(da):
    z = stats.zscore(da,ddof=1)
    T = (da-min(da))/(max(da)-min(da))
    return z,T

plt.subplots(3,2,figsize=(8,6))
a,b = zt(m_A)
plt.subplot(321)
sns.kdeplot(x=a,bw_method=0.5)
plt.title('方法A标准化分数')
plt.subplot(322)
sns.kdeplot(x=b,bw_method=0.5)
plt.title('方法A极差标准化')
c,d = zt(m_B)
plt.subplot(323)
sns.kdeplot(x=c,bw_method=0.5)
plt.title('方法B标准化分数')
plt.subplot(324)
sns.kdeplot(x=d,bw_method=0.5)
plt.title('方法B极差标准化')
e,f = zt(m_C)
plt.subplot(325)
sns.kdeplot(x=e,bw_method=0.5)
plt.title('方法C标准化分数')
plt.subplot(326)
sns.kdeplot(x=f,bw_method=0.5)
plt.title('方法C极差标准化')
plt.tight_layout()
plt.show()