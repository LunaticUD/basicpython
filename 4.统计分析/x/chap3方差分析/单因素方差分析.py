# 假设条件
# H0（零假设）：所有组别的总体均值相等，即各组之间没有显著差异。
# H1（备择假设）：至少有一组与其他组的总体均值不同，即存在显著差异。
# 为了确保单因素方差分析的有效性，通常需要满足以下前提条件：
# 独立性：各组数据应来自独立的随机样本。
# 正态性：各组数据应服从正态分布或至少接近正态分布。
# 方差齐性：不同组别的总体方差应该相等
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# 创建示例数据
data = {'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'Value': [68, 66, 65, 71, 72, 73, 74, 75, 76]}

df = pd.DataFrame(data)

# 执行单因素方差分析
model = ols('Value ~ C(Group)', data=df).fit()
anova_table = anova_lm(model, typ=2)

print("单因素方差分析结果:")
print(anova_table)
# 结果总结：
# 单因素方差分析的结果会给出F统计量 F 和P值 PR(>F)。
# 如果P值小于预先设定的显著性水平（例如0.05），则拒绝零假设，表明至少有一个组的均值与其他组有显著差异；
# 反之，则不能拒绝零假设，认为各组均值无显著差异。
# 例如，如果输出的结果是 F: 12.34, PR(>F): 0.001，
# 这意味着在0.05的显著性水平下，我们可以拒绝零假设，认为至少有一组的数据与其他组存在显著差异。
# https://lxblog.com/qianwen/share?shareId=59790d8e-972f-4be9-b52f-96611e04ea54
