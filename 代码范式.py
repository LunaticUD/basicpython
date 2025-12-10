# # ==================颜色样式范式======================
# import matplotlib.pyplot as plt
# import scienceplots
# import palettable

# # plt.style.use(['science', 'no-latex','nature'])
# plt.rcParams.update({
#     'font.family': ['Times New Roman', 'SimHei'],
#     'axes.unicode_minus': False,
#     'figure.dpi': 300,
#     'axes.linewidth':1.5,
#     "figure.figsize":(5, 5)
# })
# # cmap=Blues_8.mpl_colormap
# # palette = palettable.cartocolors.sequential.TealGrn_3.mpl_colors
# # ============================================
# # 。。。。。。
# # ==================图形创建范式======================
# # fig,ax = plt.subplots(figsize=(5,4))
# # ======================案例==========================
# import seaborn as sns
# iris_sns = sns.load_dataset("iris")
# sns.pairplot(
#     iris_sns,
#     hue='species',
#     # palette=palettable.tableau.TrafficLight_9.mpl_colors,  #Matplotlib颜色
#     # palette=palettable.colorbrewer.qualitative.Dark2_7.mpl_colors
#     # palette=palettable.cartocolors.diverging.Temps_5.mpl_colors
#     # palette=palettable.cartocolors.diverging.TealRose_3.mpl_colors
#     # palette=palettable.cartocolors.diverging.Tropic_5.mpl_colors
#     # palette=palettable.cartocolors.sequential.PinkYl_3.mpl_colors
#     # palette = palettable.cartocolors.sequential.Purp_5.mpl_colors[:3]
#     # palette = palettable.cartocolors.sequential.SunsetDark_4.mpl_colors[:3]
#     palette = palettable.cartocolors.sequential.TealGrn_3.mpl_colors
# )
# # ==================范式======================
# # ax.set_title('how2matplotlib.com')
# # ax.set_xlabel('Categories')
# # ax.set_prop_cycle('color', Dark2_7.mpl_colors)
# # ax.set_ylabel('Values')
# # ax.spines['top'].set_visible(False)
# # ax.spines['right'].set_visible(False)
# # ax.tick_params(
# #     axis='both',
# #     which='both',
# #     top=True,
# #     bottom=True,
# #     left=True,
# #     right=True
# # )
# # ax.set_xlim(0, 10)
# # ax.set_ylim(-1.2, 1.2)
# sns.despine(top=False, right=False)
# plt.tight_layout()
# plt.show()

# # =================================================================
# import numpy as np
# import numba
# import time
# @numba.njit() # 加快速度
# def cal_sum(a):
#     result = 0
#     for i in range(a.shape[0]):
#         for j in range(a.shape[1]):
#             result += a[i, j]
#     return result
# a = np.random.random((2000, 2000))
# start = time.time()
# cal_sum(a)
# end = time.time()
# print(end-start)

import matplotlib.pyplot as plt
import palettable
import scienceplots
import seaborn as sns


def plot_style_decorator(
    font_family="Times New Roman",
    font_size=12,
    figure_size=(5, 5),
    dpi=300,
    line_width=1.5,
):
    """
    装饰器用于设置matplotlib的样式，包括字体、大小、图像尺寸、dpi、线宽等。
    可以通过自定义参数来修改图表样式。
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 更新plt样式
            plt.rcParams.update(
                {
                    "font.family": font_family,
                    "font.size": font_size,
                    "axes.unicode_minus": False,
                    "figure.dpi": dpi,
                    "axes.linewidth": line_width,
                    "figure.figsize": figure_size,
                }
            )
            # 调用实际的绘图函数
            result = func(*args, **kwargs)

            # 应用seaborn的美化设置
            sns.despine(top=False, right=False)

            # 自动调整图像布局
            plt.tight_layout()
            plt.show()
            return result

        return wrapper

    return decorator


# 使用装饰器时，传入自定义的参数
@plot_style_decorator(
    font_family="Arial", font_size=14, figure_size=(7, 7), dpi=300, line_width=2
)
def create_plot():
    # 示例绘图代码
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], label="Example Line")
    ax.set_title("Example Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


# 调用装饰器修饰的绘图函数
create_plot()
print("Hello, World!")
