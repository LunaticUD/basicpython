import pandas as pd
import numpy as np
import scipy.stats as st
example6_1 = pd.read_csv("exercise\chap06\exercise6_1.csv")
x = example6_1['上网时间']
# 90%
x_int_0 = st.norm.interval(confidence=0.90,loc=np.mean(x),scale=st.sem(x))
df_0 = pd.DataFrame(np.round(x_int_0,4))
# 95%
x_int_5 = st.norm.interval(confidence=0.95,loc=np.mean(x),scale=st.sem(x))
df_5 = pd.DataFrame(np.round(x_int_5,4))
# 99%
x_int_9 = st.norm.interval(confidence=0.99,loc=np.mean(x),scale=st.sem(x))
df_9 = pd.DataFrame(np.round(x_int_9,4))
# TOTAL
df = (
    pd.DataFrame([x_int_0,x_int_5,x_int_9])
    .T
    .set_axis(['90%','95%','99%'],axis=1)
    .set_axis(['下限','上限'],axis=0)
)
print(df)