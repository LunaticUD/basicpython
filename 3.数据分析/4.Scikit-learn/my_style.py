# my_plot_style.py
import matplotlib as mpl

def set_journal_style():
    """应用期刊论文绘图样式到全局rcParams"""
    style_config = {
        # 字体与字号
        'font.family': 'serif',
        'font.serif': ['Times New Roman'],
        'font.size': 9,
        'axes.labelsize': 10,
        'axes.titlesize': 11,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 9,
        
        # 线条与标记
        'lines.linewidth': 1.0,
        'axes.linewidth': 1.0,
        'xtick.major.width': 1.0,
        'ytick.major.width': 1.0,
        
        # 图表尺寸与布局
        'figure.figsize': (8, 3.5),
        'figure.dpi': 300,
        'figure.autolayout': False,
        'savefig.dpi': 600,
        'savefig.bbox': 'tight',
        
        # 颜色与图形
        'axes.prop_cycle': mpl.cycler('color', ['#4e79a7', '#e15759', '#76b7b2']),
        'patch.linewidth': 0.8
    }
    mpl.rcParams.update(style_config)