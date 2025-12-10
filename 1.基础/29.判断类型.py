# #TODO:整型
# # 方法一
# a = eval(input())
# print(a % 1 == 0)
# # 方法二
# a = eval(input())
# print(isinstance(a,int))
# #TODO:字母
# a = "worlddd"
# print(a.isalpha())
# #TODO:数字
a = "12345"
print(a.isdigit())
print(a.isnumeric())
# #TODO:数字、字母混合
a = "woed133"
print(a.isalnum())
#TODO:判断是否是中文字符
a = "世界"
print('\u4e00' <= a <= '\u9fff')
# ** > ~ > '+\-' > * > / > // > % > +/- > <</>> > & > ^ > |
print(3*4**2//8%7)