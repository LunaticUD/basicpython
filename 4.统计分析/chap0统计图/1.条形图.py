import pandas as pd
import matplotlib.pyplot as plt
from plotnine import ggplot,aes,geom_bar,scale_fill_brewer,theme_matplotlib
import os

os.chdir('C:/Users/WZL/Documents/Text/Python/5.统计分析/Statistic_python/example/chap03')
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_csv('example3_1.csv')

# TODO:1. 简单条形图
plt.subplots(1, 2, figsize=(10, 4))  # 设置子图和图形大小
plt.subplot(121)
plt.barh(y=df['支出项目'], width=df['北京'], alpha=0.6)  # 绘制水平条形图
plt.xlabel('支出金额', size=12)
plt.ylabel('支出项目', size=12)
plt.title('（a）北京各项支出的水平条形图', size=15)
plt.xlim(0, 19000)
# 添加标签
x = df['北京']
y = df['支出项目']
for a, b in zip(x, y):
    plt.text(a + 800, b, '%.0f' % a, ha='center', va='bottom', color='black', fontsize=10)
plt.subplot(122)
labels = pd.Series(['北京', '天津', '上海', '重庆'])
h = [sum(df['北京']), sum(df['天津']), sum(df['上海']), sum(df['重庆'])]
plt.bar(x=labels, height=h, width=0.6, alpha=0.6, align='center')  # 垂直条形图
plt.xlabel('地区', size=12)
plt.ylabel('总支出', size=12)
plt.title('（b）每个地区总支出的垂直条形图', size=15)
plt.ylim(0, 55000)
# 添加标签
x = labels
y = h
for a, b in zip(x, y):
    plt.text(a, b+500, '%.0f' % b, ha='center', va='bottom', color='black', fontsize=10)
plt.tight_layout()
plt.show()

# TODO:2. 帕累托图
# 处理数据
df = df.sort_values(by='北京', ascending=False)
p = 100 * df['北京'].cumsum() / df['北京'].sum()
df['累计百分比'] = p
# 绘制条形图
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(df['支出项目'], df['北京'], color='steelblue')
ax.set_ylabel('支出金额', size=12)
ax.set_xlabel('支出项目', size=12)
ax2 = ax.twinx()
ax2.plot(df['支出项目'], df['累计百分比'], color='C1', marker='D', ms=7)
ax2.set_ylabel('累计百分比(%)', size=12)
# 添加标签
for a, b in zip(df['支出项目'], df['累计百分比']):
    plt.text(a, b + 1, '%.0f' % b, ha='center', va='bottom', color='black', fontsize=12)
plt.show()

# TODO:3. 并列条形图
plt.subplots(1, 2, figsize=(10, 4.2))
ax1 = plt.subplot(121)
df.plot(kind='bar', stacked=False, width=0.8, ax=ax1)
plt.xlabel('支出项目', size=12)
plt.ylabel('支出金额', size=12)
plt.xticks(range(8), df['支出项目'], rotation=30)
plt.title('(a)并列条形图', fontsize=13, color='black')
# TODO:4. 堆叠条形图
ax2 = plt.subplot(122)
df.plot(kind='bar', stacked=True, width=0.5, ax=ax2)
plt.xlabel('支出项目', size=12)
plt.ylabel('支出金额', size=12)
plt.xticks(range(8), df['支出项目'], rotation=30)
plt.title('(b)堆叠条形图', fontsize=13, color='black')
plt.show()
# TODO:5. 百分比条形图
my_type = pd.CategoricalDtype(categories=df['支出项目'], ordered=True)
df['支出项目'] = df['支出项目'].astype(my_type)
df = pd.melt(df, id_vars=['支出项目'], value_vars=['北京', '天津', '上海', '重庆'],
             var_name='地区', value_name='支出比例')
# 绘制
(
        ggplot(df, aes(x='地区', y='支出比例', fill='支出项目'))
        + geom_bar(stat='identity', color='black', alpha=1,
                   position='fill', width=0.8, size=0.2)
        + scale_fill_brewer(palette='Reds')
        + theme_matplotlib()
).show()