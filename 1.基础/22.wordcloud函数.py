from wordcloud import WordCloud
import jieba

txt = """
        当你感觉累的时候,你正在走上坡路。
        虽然过去不能改变，未来可以。
        只要你确信自己正确就去做。做了有人说不好，不做还是有人说不好，不要逃避批判。
        要做的事情总找得出时间和机会；不愿意做的事情也总能找得出借口。
        """
seg_list = jieba.lcut(txt)
newtxt = "".join(seg_list)
world_cloud = WordCloud(font_path="simsun.ttc").generate(newtxt)
world_cloud.to_file("we.png")
print("chengong")

gree = [1, 2, 3, 4, 5]

list1 = []
for i in range(8):  # 循环4次
    list1.append(gree)
