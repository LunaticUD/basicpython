import pandas as pd

# 1. 读入原始宽格式数据（第 1 张图那种）
# 把文件名改成你自己的
# df = pd.read_excel("D:/Work/LMM未矫正p值/脂肪酸_平均.xlsx")
# out = "D:/Work/LMM未矫正p值/脂肪酸/转好格式1.xlsx"

df = pd.read_excel("D:/Work/原始/风味物质.xlsx")
out = "D:/Work/原始/风味物质_长.xlsx"
# # df 结构大致是：
# # Group, TB1, TB2, TB3, BF1, BF2, BF3, LD1, LD2, LD3

# # 2. 转成你想要的格式（第 2 张图：Group, TB, BF, LD）
# out = pd.DataFrame({
#     "Group": df["Group"].repeat(3).values,                   # 每个组重复 3 行
#     "TB":  df[["TB1", "TB2", "TB3"]].to_numpy().ravel(),     # TB1-3 依次摊平
#     "BF":  df[["BF1", "BF2", "BF3"]].to_numpy().ravel(),     # BF1-3 依次摊平
#     "LD":  df[["LD1", "LD2", "LD3"]].to_numpy().ravel(),     # LD1-3 依次摊平
# })

# print(out)

# out.to_excel("D:/Work/LMM未矫正p值/矿物质/转好格式.xlsx", index=False)


# 宽转长：把 TB1~LD3 拉成一列
long_df = df.melt(
    id_vars=["Group"],
    value_vars=["TB1", "TB2", "TB3", "BF1", "BF2", "BF3", "LD1", "LD2", "LD3"],
    var_name="SiteRep",
    value_name="Value"
)

# 提取部位前缀
long_df["Site"] = long_df["SiteRep"].str.extract(r"([A-Za-z]+)")

# 映射：TB=1, BF=2, LD=3
site_map = {"TB": 1, "BF": 2, "LD": 3}
long_df["VAR00001"] = long_df["Site"].map(site_map)

# 如果你不需要保留 SiteRep / Site，就只留 SPSS 三列
out_spss_like = long_df[["Group", "Value", "VAR00001"]].rename(
    columns={"Value": "TB"}  # 这一列在 SPSS 里叫 TB（数值列名字随你）
)

# 3. 如需导出给 SPSS，用 Excel / CSV 保存
out_spss_like.to_excel(out, index=False)
# 或：
# out.to_csv("转好格式.csv", index=False, encoding="utf-8-sig")
