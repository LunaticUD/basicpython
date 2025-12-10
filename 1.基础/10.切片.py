# Intercept string
# string belongs to sequence,if the string is intercepted,you can use the slice method to achieve!
# string[start:end:step]
# "string"string to be intercepted
# "start"to intercept the index quoto of the first string
# "end"to intercept the index quoto of the last string
# "step"this is Slice step
# "[ ]"is before closing and then opening
# #1
str1="我爱你，China!"
Slice1=str1[0]
Slice2=str1[9]
Slice3=str1[0:3]
Slice4=str1[4:9]
print(Slice1+"\n"+Slice2+"\n"+Slice3+"\n"+Slice4)
a = input("please enter ID:")
# 130634//2001/07/10//3336
a1 = a[6:10]
a2 = a[10:12]
a3 = a[12:14]
print("你出生于" + a2 + "月 " + a3 + "日," + a1 + "年")