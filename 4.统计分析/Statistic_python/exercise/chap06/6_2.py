import numpy as np;from scipy.stats import norm;import pandas as pd

# n调查人数，x赞成人数，p赞成比例
n = 50+4;x = 32+2;p = x/n
# 大样本服从正态分布估计置信区间
int = norm.interval(confidence=0.95,loc=p,scale=np.sqrt(p*(1-p)/n))
df = (
    pd.DataFrame(np.round([int],4))
    .assign(n = 50,x = 32,p = x/n)
    .set_axis(["置信区间_下限","置信区间_上限","调查人数","赞成人数","赞成比例"],axis=1)
)
print(df)