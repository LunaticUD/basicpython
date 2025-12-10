listC = [('e', 4), ('o', 2), ('!', 5), ('v', 3), ('l', 1)]
#由元组构成的列表
print(sorted(listC, key=lambda x: x[0]))
# 
lt = ['麻省理工学院', '斯坦福大学', '哈佛大学', '加州理工学院', '芝加哥大学', '普林斯顿大学', '康奈尔大学', '耶鲁大学', '哥伦比亚大学', '宾夕法尼亚大学', '密歇根大学安娜堡分校']
print('@'.join(lt))
# 
#对序列进行操作（分别使用' '与':'作为分隔符）
seq1 = ['hello','good','boy','doiido']
print (' '.join(seq1))
print (':'.join(seq1))
#对字符串进行操作
seq2 = "hello good boy doiido"
print (':'.join(seq2))
#对元组进行操作
seq3 = ('hello','good','boy','doiido')
print (':'.join(seq3))
#对字典进行操作
seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
print (':'.join(seq4))
#合并目录
import os
print(os.path.join('/hello/','good/boy/','doiido'))