# Calculate string length
# len(string)function to calculate
# 1
string_1="I love you,China!"
length_1=len(string_1)
print(length_1)
# #2
string_2="我爱你，中国！"
tr_1=string_2.encode("utf-8")
str_1=string_1.encode("utf-8")
ength_2=len(tr_1)
length_2=len(str_1)
print(length_2)
print(ength_2)
# #3
tr_2=string_2.encode("gbk")
str_2=string_1.encode("gbk")
length_3=len(str_2)
ength_3=len(tr_2)
print(ength_3)