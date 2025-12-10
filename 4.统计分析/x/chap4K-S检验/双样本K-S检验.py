# 双样本K-S检验用来评估两个独立样本是否来自于相同但未知的分布。
# 它通过计算两个样本经验分布函数之间的最大绝对差异来构建统计量。
# 如果两组数据确实来自相同的分布，则预期这个差异会很小；反之，如果差异显著，则可能表明两个样本属于不同的分布。
from scipy.stats import ks_2samp
import numpy as np

# 生成两个不同分布的数据集
sample1 = np.random.normal(loc=0, scale=1, size=1000)  # 正态分布，均值为0，标准差为1
sample2 = np.random.uniform(-2, 2, 1000)               # 均匀分布，在[-2, 2]区间内
# 零假设 (H0)：两个样本来自相同分布。
# 备择假设 (Ha)：两个样本来自不同的分布。
# 执行双样本K-S检验
statistic, p_value = ks_2samp(sample1, sample2)
# 结果解释：如果P值小于预设的显著性水平（如0.05），则拒绝零假设，认为两个样本很可能来自不同的分布；
# 否则接受零假设，认为两个样本可能来自相同的分布。
print(f"Statistic: {statistic}, P-value: {p_value}")


