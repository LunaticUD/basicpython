import jieba
import wordcloud
import imageio.v2 as imageio
# from imageio import imread

f = open('text.txt','r',encoding='utf-8')
txt0 = jieba.lcut(f.read().replace('；','').replace('，','').replace('。',''))
txt = ' '
for i in txt0:
    if len(i) > 1:
        txt += ' '
        txt += i
mk = imageio.imread("皮卡丘.jpg")
w = wordcloud.WordCloud(
    # width=1920,
    # height=1080,  # 设置图片长宽为1080p
    # background_color='white',  # 设置背景颜色为白色
    font_path='msyh.ttf',  # 设置字体为微软雅黑
    # max_words=300,  # 设置词汇最大数量为300
    
    mask=mk,  # 设置蒙版
    colormap='magma'  # 设置配色集为magma
)
w.generate(txt)
w.to_file("pywordcloud.png")