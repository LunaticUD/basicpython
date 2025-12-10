import pandas as pd
import numpy as np
import scipy.stats as st
from statsmodels.stats.weightstats import ttest_ind
example6_3 = pd.read_csv("exercise\chap06\exercise6_3.csv")
x1 = example6_3['方式1'];x2 = example6_3['方式2']
# 第一梯队
print("-----第一梯队-----")
int1 = st.norm.interval(0.95,loc=np.mean(x1),scale=st.sem(x1))
int2 = st.t.interval(0.95,len(x1)-1,loc=np.mean(x1),scale=st.sem(x1))
df1 = (
    pd.DataFrame(np.round(int1,4))
    .T
    .set_axis(['下限','上限'],axis=1)
)
df2 = (
    pd.DataFrame(np.round(int2,4))
    .T
    .set_axis(['下限','上限'],axis=1)
)
print("大样本")
print(df1)
print("小样本")
print(df2)
# 第二梯队
print("-----第二梯队-----")
s = x2.var();n = len(x2)

LCI = (n-1)*s/st.chi2.ppf(q=1.95/2,df=n-1)
UCI = (n-1)*s/st.chi2.ppf(q=0.05/2,df=n-1)
print(f'第二种排队方式等待时间方差95%置信区间为：[{LCI:.5f}, {UCI:.5f}]')
# 第一第二梯队
print("-----第一第二梯队-----")
xbar1 = x1.mean();xbar2 = x2.mean()
# 假定方差相等
t_value,p_value,df = ttest_ind(x1=x1,x2=x2,alternative='two-sided',usevar='pooled')
int1 = st.t.interval(confidence=0.95,df=df,loc=(xbar1-xbar2),scale=(xbar1-xbar2)/t_value)
df3 = (
    pd.DataFrame(np.round(int1,4))
    .T
    .assign(method1=xbar1,method2=xbar2,ddof=df)
    .set_axis(['下限','上限','方法一','方法二','自由度'],axis=1)
    .set_axis(['时间(min)'],axis=0)
    
)
print(df3)
# 假定方差不相等
t_value,p_value,df = ttest_ind(x1=x1,x2=x2,alternative='two-sided',usevar='unequal')
int2 = st.t.interval(confidence=0.95,df=df,loc=(xbar1-xbar2),scale=(xbar1-xbar2)/t_value)
df4 = (
    pd.DataFrame(np.round(int2,4))
    .T
    .assign(method1=xbar1,method2=xbar2,ddof=df)
    .set_axis(['下限','上限','方法一','方法二','自由度'],axis=1)
    .set_axis(['时间(min)'],axis=0)
    
)
print(df4)