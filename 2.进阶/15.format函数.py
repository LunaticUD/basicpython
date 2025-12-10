# Format函数
import math
# 基本语法是通过 {} 和 : 来代替以前的 %
my = ["百度", "www.baidu.com"]
print("网站：{0[0]}".format(my) + "\n" + "网址：{0[1]}".format(my))  # 使用+替代，可以解决输出整齐问题
# 数据格式
# 保留小数点后两位 {:.2f}.format()
print("{:.2f}".format(math.pi))
# 带符号保留小数点后两位 {:+,-... .2f}.format()
print("{:+.2f}".format(math.pi))    # +
print("{:-.2f}".format(-math.pi))   # -
print("{:.0f}".format(math.pi))     # 不带小数
# 格式补充
print("{:0>2d}".format(3), "{:+>2d}".format(3))          # >左边补 零/其他符合 2个宽度 数在右
print("{:0<4d}".format(3), "{:+<10d}".format(3))         # <右边补 零/其他符合 4/10个宽度  数在左
# 数字优化
print("{:,}".format(30000000))      # 逗号分隔
print("{:.2%}".format(0.252))       # 百分比格式
print("{:.2e}".format(30000000))    # 指数记法
# 对齐
print("{:>10d}".format(3))          # 右对齐   数在右
print("{:<10d}".format(3))          # 左对齐   数在左
var = input()
print("{:*^10}".format(var))          # 中间对齐
# 进制
print('{:b}'.format(11))            # 二进制
print('{:d}'.format(11))            # 十进制
print('{:o}'.format(11))            # 八进制
print('{:x}'.format(11))            # 十六进制
print('{:#x}'.format(11))
print('{:#X}'.format(11))
