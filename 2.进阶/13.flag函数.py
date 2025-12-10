# ls=[1,2,3,4,5,6,7,8,9]
# print(type(str(ls).strip("[]").split(",")))
# print(" ".join(str(ls)))
# flag用于告诉计算机标记
# 字符串查找 string.find()——>第一个元素出现的位置
# 字符串的替换words[i]=namelist[j][0]
flag = True
for i in range(10):
    if i>=3:
        flag = False
    if flag==False:
        print(i)