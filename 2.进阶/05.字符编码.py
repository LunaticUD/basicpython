# 字符编码
# ord()获取字符的整数表示，chr()将编码转换为对应的字符
print(ord('中'),ord('文'))
print(chr(20013)+chr(25991))
print('\u4e2d\u6587')
# str通过encode编码为指定的字节,通过decode解码为指定的str
a = '中文'.encode('utf-8')
print(a)
b = a.decode('utf-8')
print(b)
# len()可以计算str中有多少个字符
print(len(a),len(b))

print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(97))

# 详细

#TODO: ####################用encode（）方法编码########################### #
# str.encode([encoding="utf-8"][,errors="strict"])
# str:表示要进行转化的字符串
# encoding="utf-8"：可选参数，用于指定在转码时需要采用的编码，默认为“utf-8”，如果要使用简体中文，
# 也可以使用为gb2312,当只有这一个参数时，可以省略前面的“encoding=”，直接写编码。
# errors="strict"：可选参数，用于指定错误处理方式，其可选择的值有strict（遇到非法字符就抛出异常）、ignore（忽略非法字符）、
# replease（用“？”替换非法字符）或xmlcharrefreplace（使用xml的字符引用）等。默认为strict。
verse="我爱你，中国！"                       #原字符，默认为utf-8格式
byte=verse.encode("gbk")                    #原字符编码为gbk格式
print("verse的gbk格式",byte)                #打印出来
byt=verse.encode("utf-8")                   #gbk格式编码为utf-8格式
print("verse的utf-8格式",byt)               #打印出来为
#TODO: #####################用decode（）方法解码##########################
# bytes.decode([encoding="utf-8"][,errors="strict"])
# bytes：表示要进行转换的二进制数据
# encoding="utf-8":可选参数，用于指定在编码时所采用的字符编码，默认为utf-8，如果想使用简体中文，也可以设置为gb2312，
# 当只有这一个参数时，可以省略前面的encoding直接写字符编码。
# errors="strict":Optional parameters,used to specify error handing.where the selectable values are "strict"
# (throw an exception when encountering an illegal value)
# "ignore"(Ignore illegal characters),"replace"(Replace illegal characters with "?"),or "xmlcharrefreplace"
# (Use XML character references),but the default value is "strict"
byte_1=byte.decode("gbk")                   #对上面的verse的gbk格式进行解码
print(byte_1)                               #打印出来
byte_2=byt.decode("utf-8")                  #对上面的byte的utf-8进行解码
print(byte_2)                               #打印出来

# 详细

#TODO: 格式语法为chr(<数值表达式>)
# 函数返回值类型为string，其数值表达式值的取值范围为0-255
# chr(i)
# i可以是10进制也可以是16进制形式的数字
# 返回当前整数对应的ASII字符
# j = 0
# c = 0
# for i in range(256):
#     j = j + 1
#     c = c+1
# 1# print(j, chr(i), end='\n')
#     ls1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     ls2 = ['A', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
#     'C','V', 'B', 'N', 'M']
#     ls3 = []
#     for z in ls2:
#         s = z.lower()
#         ls3.append(s)
#     if chr(i) in ls1:
#         print(ls1, end='')
#         print('is', j)
#         pass
#     elif chr(i) in ls2:
#         print(ls2, end='')
#         print('is', j)
#         pass
#     elif chr(i) in ls3:
#         print(ls3,end='')
#         print('is',j)
#         pass
#     else:
#         continue
# ls2 = ['A', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
#        'V', 'B', 'N', 'M']
# ls3 = []
# for z in ls2:
#     s = z.lower()
#     ls3.append(s)
# print(ls3)
#TODO: ###########################ord()函数
# ord("字符串")
# 函数返回值类型为int()类型
# org("0"),结果显示：48
# org()是chr()（对于8位的ASII字符串）或unichr()（对于Unicode对象）的配对函数
# 它以一个字符（长度为1的字符串）作为参数，返回对应的ASII数值，或者Unicode数值，所给Unicode字符超出python定义范围，则会引发一个typeerror异常
# 语法org(c),c-字符
# org()就好比是获取某字符的索引数
# a = ord('a')
# print(a)
print(ord("0"))
print(chr(48))