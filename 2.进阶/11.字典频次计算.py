f = open("name.txt")
names = f.readlines()
f.close()
f = open("vote.txt")
votes = f.readlines()
f.close()
f.close()
f = open("vote1.txt", "w")
D = {}
NUM = 0
for vote in votes:  #
    num = len(vote.split())  #
    if num == 1 and vote in names:  #
        D[vote[:-1]] = D.get(vote[:-1], 0) + 1  # # 字典频次
        NUM += 1  #
    else:  #
        f.write(vote)  #
f.close()
l = list(D.items())  # 字典转化为列表嵌套元组
l.sort(key=lambda s: s[1], reverse=True)  # 列表逆排序
name = l[0][0]
score = l[0][1]
print("有效票数为：{} 当选村长村民为:{},票数为：{}".format(NUM, name, score))
