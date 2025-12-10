# 去除字符串中的空格和特殊字符
# 1.strip()方法
# str.strip([chars])
# 去除字符串两侧空格和特殊字符
# chars为指定要去除的字符
s = '@ 我不知道明天会发生什么 @'
print(s)
print(s.strip('@'))
# 2.lstrip()方法
# 去除字符串左侧特殊字符或空格
s = '@ 我不知道明天会发生什么 @'
print(s)
print(s.lstrip('@ '))
# 3.rstrip()方法
# 去除字符串右侧的特殊字符或空格
s = '@ 我不知道明天会发生什么 @'
print(s)
print(s.rstrip('@ '))