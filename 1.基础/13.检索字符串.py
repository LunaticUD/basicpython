# 检索字符串
# 1.count()方法
# str.count(sub[,start[,end]])
# str:表示原字符串
# sub:表示要检索的子字符串
# start:可选参数，表示要检索范围的起始位置的索引,不指定，从头开始。
# end:可选参数，表示检索范围的结束位置的索引，不指定，一直检索到结尾
# 检索子字符串在指定字符串出现的次数，返回的时子字符串出现的次数
str1 = 'R中秋节 R快乐 R祝愿 R所有人 R平安 R健康'
print('子字符串R出现了', str1.count('R'), '次')
# 2.find()方法
# str.find(sub[,start[,end]])
# 其语法同count（）方法
# 检索是否包含指定的子字符串，不存在返回-1，存在返回首次出现该子字符串的索引
str1 = '中秋节 快乐 R祝愿 R所有人 R平安 R健康'
print('子字符串R首次出现在',str1.find('R'),'的索引位置')
# 3.index()方法
# 其语法格式与用法同find()方法
# 但是在不存在的子字符串下，会抛出异常
str1 = 'R中秋节 R快乐 R祝愿 R所有人 R平安 R健康'
print('子字符串出现在',str1.index('R'))
print(str1.index('.'))
# 4.startswith()方法
# str.startswith(prefix[,start[,end]])
# 其用法同上
# 但是检索的是字符串是否以子字符串开头，返回True/False
str1 = 'R中秋节 R快乐 R祝愿 R所有人 R平安 R健康'
print('字符串是否以R开头',str1.startswith('R'))
# 5.endswith()方法
# 同startswith（）方法
# 判断的是字符串是否是以子字符串结尾的
str1 = 'R中秋节 R快乐 R祝愿 R所有人 R平安 R健康'
print('字符串是否以R开头',str1.endswith('R'))