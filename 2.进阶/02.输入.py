# # 输入
# name = input("what is your name?")
# print("Hello!",name)
# # 对象输入的是字符串
# age = int(input("年龄："))
# if age>=20:
#     print('xxxx')
#     print('......')
# for i in range(1,10):  #打印乘法口诀表
#     j=1
#     while (j<=i):
#         print (str(j)+'*'+str(i)+'=',j*i,end=' ')#不能用‘+’只能用‘，’来使他不换行
#         j=j+1
#     print ('\n')  
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end=' ')
        i += 1
    print(' ')
print("你好啊！")