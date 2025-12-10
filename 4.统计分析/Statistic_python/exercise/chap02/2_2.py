import pandas as pd
import random

data = pd.read_csv('exercise2_2.csv')
print(data.sort_values('数学', ascending=False))
name = data['姓名']
print("有放回：", random.choices(population=name, k=5))
print("无放回：", random.sample(population=list(name), k=5))
print('经济学专业女生：' + '\n', data[(data['专业'] == '经济学') & (data['性别'] == '女')])
print('统计学分数大于等于90的男生：' + '\n', data[(data['统计学'] >= 90) & (data['性别'] == '男')])
