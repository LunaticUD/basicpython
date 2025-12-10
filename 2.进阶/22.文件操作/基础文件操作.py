# 文件操作需要open()函数来进行
# f为句柄，负责操纵你打开文件
#           路径    查看文件方式        编码格式(文字类型都要加上一个encoding="")
# 路径分为绝对与相对路径，其中相对路径用的比较多
# 绝对路径就是那个盘下的那个文件
# 相对路径就是相对与程序的文件夹，目标文件在哪里，不在同一个文件夹要出来，需要../出来一层../../出来两层下的那个文件

# 文件操作的基本
# f = open("./03.text.txt", mode="r", encoding="utf-8")
# print(f.read())

# # r: 只读模式
# f = open("../text.txt",mode="r",encoding="utf-8")
# 1.r.read(),把文件内容全部读出来,r.read(3),读取文件的前3个字符,后一种方法比前一种要好，防止压迫内存，但是却不知道要读取多少字符
# print(f.read())
# print(f.read(5))
# f.close()
# # 2.r.readline(),把文件一行一行的读出来,但是会存在空行，是由于print的换行和文件的换行符存在导致的，但是不知道要读取多少行
# print(f.readline())
# print(f.readline())
# f.close()
# # 3.for循环 🍵
# print(f)    # <_io.TextIOWrapper name='./03.text.txt' mode='r' encoding='utf-8'>
# for i in f:
#     print(i, end='')            # 但是会有空行
#     print(i.strip())            # 通过strip函数来去掉空白
# # 4.第一行单独读取
# first = f.readline()
# print(first)
# print("==================")
# for i in f:
#     print(i.strip())

# # w:write只写模式，没有文件会重新创建出一个文件，不论源文件内是否有数据存在，都会被重写
# f = open("./04.text1.txt", mode="w", encoding="utf-8")
# f.write("我爱你！")
# f.write("\n")
# f.write("中国")
# f.close()

# # a:append 追加写模式，不会重新创建文件，只会在文件不存在时创建文件
# f = open("./04.text1.txt", mode="a", encoding="utf-8")
# f.write("我爱你中国")
# f.close()

# # b:bytes,二进制，一般处理非文本文件，==不能指定encoding==
# # 包括rb,读取操作,wb,写入操作，两者结合可以完成文件的复制粘贴操作
# f = open("C:/Users/32230/OneDrive/图片/本机照片/山.jpg",mode="rb")
# f1 = open("../山.jpg",mode="wb")
# f1.write(f.read())
# f.close()

# +:扩展模式，r+,w+,a+,r+b,w+b,a+b,
# 容易出问题

# 文件操作的另一种写法

# with open("./03.text.txt", mode="w", encoding="utf-8") as f:
#     f.write("xxx")

# #                   with语句的代码块最后会再with程序终止时有f.close()操作

# 当文件有两个时可以如下操作
# with open("../text.txt", mode="w", encoding="utf-8") as f1, \
#         open("../text1.txt", mode="w", encoding="utf-8") as f2:
#     f1.read()
#     f2.write("xxx")


# 文件操作必备技能
# 文件的修改
# with open("../text.txt",mode="r",encoding="utf-8") as f1:
#     f1.readline()
#     if * in f1.readline():
#         i =


# 读取规则的文件
# # readlines()函数，返回列表
# f = open("Python\VI.思想内容\city.csv","r",encoding='utf-8')
# ls = f.read().split(',')
# rs = f.readlines()      # 返回列表
# f.close()
# print(ls)
# print(rs)
# # writelines()函数
# fo=open("text.csv",'w',encoding='utf-8')
# x=['春眠','处处','夜来']
# fo.writelines(x)
# fo.close()
# # fo.tell()函数
# fo=open("text.csv",'r',encoding='utf-8')
# print(fo.tell())
# print(fo.read())
# print(fo.tell())
# fo.seek()函数

fo=open("text.csv",'r',encoding='utf-8')
print(fo.tell())
fo.seek(3)
print(fo.read())
print(fo.tell())