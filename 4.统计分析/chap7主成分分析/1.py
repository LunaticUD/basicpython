import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer
from sklearn.preprocessing import StandardScaler

# 1. 数据加载与预处理
data = pd.read_csv('6.统计分析\chap7主成分分析\wheat.txt')
data = data.dropna()  # 删除缺失值
scaler = StandardScaler(with_mean=True, with_std=True)  # 样本标准差
data_scaled = scaler.fit_transform(data)
data_scaled = pd.DataFrame(data_scaled, columns=data.columns)

# 2. 使用与SAS相同的因子数量和旋转方法
n_factors = 5  # 根据SAS结果设置
fa = FactorAnalyzer(n_factors=n_factors, rotation='promax', method='ml')  # 斜交旋转+最大似然
fa.fit(data_scaled)

# 3. 输出因子载荷矩阵
loadings = fa.loadings_
print("因子载荷矩阵：")
print(pd.DataFrame(loadings, index=data.columns, columns=[f'Factor{i+1}' for i in range(n_factors)]))

# 4. 手动计算因子得分（Bartlett法）
score_coef = fa.loadings_.T @ np.linalg.inv(fa.corr_)
factor_scores = data_scaled.values @ score_coef.T
factor_scores_df = pd.DataFrame(factor_scores, columns=[f'Factor{i+1}' for i in range(n_factors)])
print("因子得分示例：")
print(factor_scores_df.head())