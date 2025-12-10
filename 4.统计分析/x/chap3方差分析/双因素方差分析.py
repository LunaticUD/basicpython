# 假设条件
# H0（零假设）：对于每个因素及其交互作用，各水平下的总体均值相等。
# H1（备择假设）：至少有一个因素或交互作用中的某水平与其他水平的总体均值不同。
# 多因素方差分析除了上述前提条件外，还需要考虑因素间的交互效应是否显著。
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import os

os.chdir('D:\\Text\\CODE\\Python\\8.统计分析\\chap3方差分析')
data = 'txt.csv'

df = pd.read_csv(data, names=['gender', 'education', 'Index'])
print(df.head())
# 方差分析
anova = smf.ols('Index ~ C(gender) + C(education) + C(gender)*C(education)',data = df).fit()
print(sm.stats.anova_lm(anova, typ=1))
# 事后多重比较
print(sm.stats.multicomp.pairwise_tukeyhsd(groups = df.education, endog=df.Index).summary())


