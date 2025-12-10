import pandas as pd
import os

os.chdir('D:\Text\Statistic_python\exercise\chap05')

da = pd.read_csv("exercise5_1.csv")
print("有2-5台冷气机出现缺陷的概率：",da.query("2<=X<=5")['P'].sum())
print("有不到2台冷气机出现缺陷的概率：",da.query("X<2")['P'].sum())
print("有超过5台冷气机出现缺陷的概率：",da.query("5<X")['P'].sum())