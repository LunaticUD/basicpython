import matplotlib.pyplot as plt
import numpy as np

# 科研期刊样式参数 (字典格式)
JOURNAL_STYLE = {
    # 字体与字号
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],  # 主字体
    'font.size': 9,                     # 全局字号
    'axes.labelsize': 10,               # 坐标轴标签
    'axes.titlesize': 11,               # 标题字号
    'xtick.labelsize': 9,               # X轴刻度
    'ytick.labelsize': 9,               # Y轴刻度
    'legend.fontsize': 9,               # 图例字号
    
    # 线条与标记
    'lines.linewidth': 1.0,            # 线宽
    'axes.linewidth': 1.0,             # 坐标轴线宽
    'xtick.major.width': 1.0,          # X刻度线宽
    'ytick.major.width': 1.0,          # Y刻度线宽
    
    # 图表尺寸与布局
    'figure.figsize': (8, 3.5),        # 图表尺寸 (宽,高)
    'figure.dpi': 300,                 # 显示分辨率
    'figure.autolayout': False,        # 禁用自动布局
    'savefig.dpi': 600,                # 保存分辨率
    'savefig.bbox': 'tight',           # 去除白边
    
    # 颜色与图形
    'axes.prop_cycle': plt.cycler('color', ['#4e79a7', '#e15759', '#76b7b2']),  # 颜色循环
    'patch.linewidth': 0.8,            # 图形边框线宽
}
plt.rcParams.update(JOURNAL_STYLE)

# 原始数据
data = [
    77, 78, 44, 85, 42, 80, 51, 62, 60, 105, 63, 95, 85, 75, 107, 62, 79, 63,
    107, 109, 92, 72, 65, 86, 55, 91, 77, 82, 81, 102, 95, 54, 78, 79, 57, 37,
    105, 63, 83, 68, 79, 71, 75, 73, 85, 73, 59, 75, 91, 114, 38, 37, 78, 104,
    91, 40, 61, 73, 77, 66, 73, 39, 30, 131, 133, 68, 92, 53, 38, 85, 43, 113,
    63, 69, 85, 63, 82, 96, 83, 74, 121, 52, 81, 26, 72, 58, 77, 76, 56, 78,
    53, 75, 111, 50, 94, 63, 41, 104, 104, 53
]

# 创建画布
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# ----------------------------
# 箱线图（左）
# ----------------------------
# 绘制箱线图
box = ax1.boxplot(data, patch_artist=True, widths=0.6)

# 设置箱线颜色
box['boxes'][0].set_facecolor('lightblue')   # 箱体填充色
box['medians'][0].set_color('red')           # 中位线颜色
box['whiskers'][0].set_color('black')        # 须线颜色
box['whiskers'][1].set_color('black')

# 简化坐标轴
ax1.set_xticks([])  # 隐藏x轴刻度
ax1.set_ylabel('Values')
ax1.set_title('Boxplot', pad=10)

# ----------------------------
# 小提琴图（右）
# ----------------------------
# 绘制小提琴图
vp = ax2.violinplot(data, showmeans=True)

# 设置小提琴颜色
vp['bodies'][0].set_facecolor('lightgreen')
vp['bodies'][0].set_edgecolor('black')
vp['bodies'][0].set_alpha(0.7)
vp['cmeans'].set_color('darkred')  # 均值线颜色

# 简化坐标轴
ax2.set_xticks([])  # 隐藏x轴刻度
ax2.set_title('Violin Plot', pad=10)

# ----------------------------
# 通用设置
# ----------------------------
# 统一y轴范围
ymin, ymax = np.min(data)-5, np.max(data)+5
ax1.set_ylim(ymin, ymax)
ax2.set_ylim(ymin, ymax)

# 隐藏顶部和右侧边框
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)  # 隐藏底部边框
    
plt.tight_layout()
plt.show()
plt.savefig("mixed_fonts1.png", bbox_inches='tight')