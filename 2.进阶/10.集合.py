# set 
# set是一组key的集合
s = set({'a':1})
# s = set((1,2,3)) # -->s = set([1,2,3])
print(s)
# set内元素不可重复
s = set([1,1,2,2,3,3,3,4,6,5])
print(s)
# 添加元素
s.add('a')
print(s)
# 删除元素
s.remove('a')
print(s)
# &、| <==>交、并
s = set([1,1,2,2,3,3,3,4,6,5])
a = set([5,6,7,8,9,4])
print(s&a,s|a)