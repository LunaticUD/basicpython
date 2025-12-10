# my_plot_style.py
import matplotlib as mpl

def set_journal_style():
    """应用期刊论文绘图样式到全局rcParams"""
    style_config = {
        # =====字体与字号 =====
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'SimSun'],
        'axes.unicode_minus':False,    # 负号显示
        'font.size': 9,
        'mathtext.fontset': 'stix',
        'axes.labelsize': 10,
        'axes.titlesize': 11,
        
        # =====线条与标记 =====
        'lines.linewidth': 1.5,
        'axes.linewidth': 1.2,
        'xtick.major.width': 1.2,
        'ytick.major.width': 1.2,
        'xtick.direction': 'in',  # 刻度朝内
        'ytick.direction': 'in',
        
        # =====图表尺寸与布局 =====
        'figure.figsize': (6.5, 6.5),
        'figure.autolayout': True,  # 自动防溢出
        'figure.dpi': 300,
        'savefig.dpi': 600,
        'savefig.format': 'pdf',  # 矢量图更受期刊欢迎
        'savefig.bbox': 'tight',
        
        # ===== 颜色与图形 =====
        'axes.prop_cycle': mpl.cycler('color', [
            '#2F4F4F',  # 优化为CMYK友好的颜色
            '#CD5C5C',  # ['#4e79a7', '#e15759', '#76b7b2']
            '#6A5ACD'
        ]),
        'patch.linewidth': 1.0,
        'grid.linewidth': 0.6,  # 按需添加网格线
        'grid.alpha': 0.3,
        
        # ===== 图例与标注 =====
        'legend.fontsize': 8,
        'legend.frameon': True,
        'legend.framealpha': 0.8,
        'legend.edgecolor': 'black'
    }
    # # 启用LaTeX数学模式（可选）
    # if False:  # 设为True需要系统安装LaTeX
    #     style_config.update({
    #         'text.usetex': True,
    #         'text.latex.preamble': r'\usepackage{amsmath}'
    #     })
    mpl.rcParams.update(style_config)