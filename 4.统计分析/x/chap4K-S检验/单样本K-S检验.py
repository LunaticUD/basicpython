# 单样本K-S检验用于测试一个样本是否来自已知的理论分布，如正态分布、均匀分布等。
# 它比较的是样本的经验分布函数（ECDF）与指定理论分布之间的最大绝对差异。该检验对连续型数据特别有用，并且不需要对数据做任何参数假设。
from scipy.stats import kstest
import numpy as np

# 生成一组服从标准正态分布的数据
data = np.random.normal(0, 1, 1000)
# 零假设 (H0)：样本来自指定的理论分布。
# 备择假设 (Ha)：样本不是来自指定的理论分布。
# 对数据进行K-S检验，判断其是否来自标准正态分布
statistic, p_value = kstest(data, 'norm')
# 结果解释：如果P值小于预设的显著性水平（如0.05），则拒绝零假设，认为样本不来自该理论分布；否则接受零假设，认为样本可能来自该分布。
print(f"Statistic: {statistic}, P-value: {p_value}")
