# Jieba库
# pip install jieba
import jieba
# # # #TODO:精确模式
# x = jieba.cut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎')
# # print(x)    # 返回<generator object Tokenizer.cut at 0x0000024C4E650740>迭代器
# for i in x:
#     print(i, end='\\')
#     pass
# # print(jieba.lcut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎'))  # 返回列表
# # #TODO:全模式
# x = jieba.cut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎', cut_all=True)
# # print(x)
# for i in x:
#     print(i, end='\\')
#     pass
# y = jieba.lcut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎', cut_all=True)
# print('/'.join(y))
# #TODO:搜索引擎模式
# x = jieba.cut_for_search('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎')
# # print(x)
# for i in x:
#     print(i, end='\\')
#     pass
# print(jieba.lcut_for_search('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎'))
# # #TODO:词频、添加新词
# x = jieba.cut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎')
# jieba.add_word('最大的')
# # print(x)
# for i in x:
#     print(i, end='\\')
#     pass
# print(jieba.lcut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎').count('最大'))
# # 添加字典
# jieba.load_userdict('./add.txt')
# x = jieba.cut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎')
# print('/'.join(x))
# # 删除新词
# jieba.load_userdict('./add.txt')
# jieba.del_word('最大的骄傲')
# x = jieba.cut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎')
# y = '/'.join(x)
# print(y)
# # 处理停用词
# stop = ['的']
# x = jieba.cut('最大的骄傲于最大的自卑都表示心灵的最软弱无力。——斯宾诺莎')
# for i in x:
#     if i not in stop:
#         print(i, end='/')
#         pass
#     pass
# 权重分析
di = ['，', '：', '。', ' ', '、', '“', '”', '！', '？', '：', '；']
with open('./我的家乡.txt', mode='r',encoding='utf-8') as f:
    chars = f.read()
    for k in ' ，。“‘’”：！、《》；？　」「…":':
        char = chars.replace(k, "").replace('\n', "")
    tag = jieba.lcut(char)
    # dicts = {}
    new_tag = []
    for i in tag:
        if i not in di:
            new_tag.append(i)
    for a in range(len(new_tag)):
        j = new_tag.count(new_tag[a])
        # dicts[j] = new_tag[a]
        print('{0:<}{1:>}'.format(new_tag[a], j))
# 反向思维
f = open('data.txt','r')
lines=f.readlines()
f.close()
D=[]
for line in lines:
    wordList=jieba.lcut(line)   #用结巴分词，对每行内容进行分词
    for word in wordList:
        if len(word)<3:         #判断词长度，要大于等于3个长度
            continue
        else:
            if word not in D:       #@#@#@@@@ 反向判断值是否在空列表中，从而获得不重复的列表
                D.append(word)
f=open('out1.txt','w')
f.writelines('\n'.join(D))            
f.close()