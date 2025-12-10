import pandas as pd
import numpy as np

data = pd.read_csv('exercise2_5.csv')
print(data)
# 确定组别
sec = 1 + round(np.divide(np.log10(100), np.log10(2)))
# 确定组距
sed = np.floor(np.divide(data.max() - data.min(), sec)).iloc[0]
# 分组
bins = np.arange(data.min().iloc[0] - 1, data.max().iloc[0] + sed, sed)
f = pd.cut(data['使用寿命'], bins=bins, right=True)
tab = f.value_counts().sort_index()
df = pd.concat({"频数": tab}, axis=1)
df.loc[:, '频数百分比（%）'] = (df['频数'] / sum(df['频数'])) * 100
df.loc[:, '累积频数'] = df['频数'].cumsum()
df.loc[:, '累积频数百分比（%）'] = (df['频数'].cumsum() / df['频数'].sum()) * 100
df.index.name = '使用寿命（小时）'
print(round(df, 2))
