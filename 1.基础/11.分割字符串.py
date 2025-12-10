# 分割字符串
# str.split(sep,maxsplit)
# str表示要进行分割的字符串
# sep用于指定分隔符，可以包含多个字符，默认为None，即所有字符（包括空格，换行“\n”,制表符“\t”）
# maxsplit可选参数，用于指定分割的次数，如果不指定或者为-1，则分割次数没有限制，否则返回结果列表的元素个数为maxsplit+1
str1="中 秋 节 快 乐 >>> 祝 愿 所 有 人 平 安 健 康"
a=str1.split()
b=str1.split(' ',4)
c=str1.split('>>>')
print(a)
print(b)
print(c)

print(len(['']))