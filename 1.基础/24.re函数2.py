# 练习

import re

#提取出python
key="javapythonc++php"
re.findall('python',key)[0]            # 都有引号

#提取出hello world
key="<html><h1>hello world<h1></html>"
re.findall('<h1>(.*)<h1>',key)[0]

#提取170
string = '我喜欢身高为170的女孩'
re.findall('\d+',string)

#提取出http://和https://
key='http://www.baidu.com and https://boob.com'
re.findall('https?://',key)

#提取出hello
key='lalala<hTml>hello</HtMl>hahah' #输出<hTml>hello</HtMl>
re.findall('<[Hh][Tt][mM][lL]>(.*)</[Hh][Tt][mM][lL]>',key)

#提取出hit.
key='bobo@hit.edu.com'            #想要匹配到hit.
re.findall('h.*?\.',key)

#匹配sas和saas
key='saas and sas and saaas'
re.findall('sa{1,2}s',key)

#匹配出i开头的行
string = '''fall in love with you
i love you very much
i love she
i love her'''
re.findall('^i.*',string,re.M)

#匹配全部行
string1 = """<div>静夜思
窗前明月光
疑是地上霜
举头望明月
低头思故乡
</div>"""
re.findall('.*',string1,re.S)


# 爬取糗事百科中所有糗图照片

import requests
import re
import os

#创建一个文件夹
if not os.path.exists('./qiutuLibs'):        # 注意里面要有引号
    os.mkdir('./qiutuLibs')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

url = 'https://www.qiushibaike.com/pic/'
page_text = requests.get(url=url,headers=headers).text

#进行数据解析（图片的地址）
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'        #不相关的可以用.*，非贪婪匹配

#re.S单行匹配
src_list = re.findall(ex,page_text,re.S)
print(src_list)

for src in src_list:
    src = 'https:'+src                                #发现src属性值不是一个完整的url，缺少了协议头

#对图片的url单独发起请求，获取图片数据.content返回的是二进制类型的响应数据
    img_data = requests.get(url=src,headers=headers).content
    img_name = src.split('/')[-1]                            # url 最后一个斜杠的就是图片名
    img_path = './qiutuLibs/'+img_name
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,'下载成功！')
