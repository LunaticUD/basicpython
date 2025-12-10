import pandas as pd

data = pd.read_csv('exercise2_4.csv')
print(data)
# TODO 1
print('性别简单频数表：')
print(data['性别'].value_counts())
print('满意度简单频数表：')
print(data['满意度'].value_counts())
# TODO 2
print('性别满意度二维列联表：')
print(pd.crosstab(data['性别'], data['满意度']))
# TODO 3
print('性别满意度二维列联表：（百分比）')
tab1 = pd.crosstab(data['性别'], data['满意度'], margins=True, margins_name='合计', normalize='all')
print(tab1*100)
