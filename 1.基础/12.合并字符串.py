# 合并字符串
# strnew=string.join(iterable)
# strnew:表示合并后形成的新字符串
# string：字符串类型，用于指定合并时的分隔符
# iterable：可迭代对象，该迭代对象中的所有元素(字符串表示)将被合并为一个新的字符串，string作为一个分界点被分割出来
a=['中秋节','八月十五']
strnew=' @'.join(a)
print('@'+strnew)