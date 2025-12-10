import pandas as pd

df = pd.read_excel('02.xlsx',sheet_name=0)
# df['日期'] = pd.to_datetime(df['日期'],origin='1900-01-01')
print(df)
# 规律修改
df.index = range(11,len(df)+11)
print(df)
# pd.index
df.index = pd.Index(['A','B','C','D'])
print(df)
# 直接修
df.index = ['一','二','三','四']
print(df)