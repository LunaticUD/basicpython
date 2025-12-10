# TODO:独立样本T检验
from scipy.stats import ttest_ind
from scipy.stats import levene

# 两个独立样本数据
data1 = [5.1, 4.9, 5.0, 5.2, 4.8, 5.1, 5.0]
data2 = [4.8, 4.7, 4.9, 4.6, 5.0, 4.9, 4.8]
# H0（零假设）：两个样本的均值相等（无显著差异）
# H1（备择假设）：两个样本的均值不相等（有显著差异）
# 检查方差齐性
leve_test_result = levene(data1, data2)
if leve_test_result.pvalue > 0.05:
    # 方差齐性成立
    equal_var = True
else:
    # 方差不齐
    equal_var = False
# 进行独立样本T检验
t_statistic, p_value = ttest_ind(data1, data2, equal_var=equal_var)
t_result = f"T-statistic: {round(t_statistic,3)}, P-value: {round(p_value,3)}"
# 结果
if round(p_value, 3) < 0.05:
    print(f"{t_result},p值<0.05，因此拒绝原假设，两个样本的均值差异显著，即认为两个样本的均值不相同。")
else:
    print(f"{t_result},p值>0.05，因此拒绝备译假设，两个样本的均值差异不显著，即认为两个样本的均值相同。")
