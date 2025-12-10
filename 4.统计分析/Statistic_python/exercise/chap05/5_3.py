import pandas as pd
from scipy.stats import norm

print("-----------(1)----------")
print("P(X>=510)=",round(1-norm.cdf(510,500,20),6))
print("P(400<=X<=450)=",round(norm.cdf(450,500,20)-norm.cdf(400,500,20),6))
print("-----------(2)----------")
print("P(0<=Z<=1.2)=",round(norm.cdf(1.2)-norm.cdf(0),6))
print("P(-4.8<=Z<=0)=",round(norm.cdf(0)-norm.cdf(-0.48),6))
print("P(1.2<=Z)=",round(1-norm.cdf(1.2),6))
print("-----------(3)----------")
print("标准正态分布累计概率为0.95时的分位数值z=",round(norm.ppf(0.95),6))