# NOTE:将离散概率问题转换为可测函数的集合问题
from collections import defaultdict
from pandas import DataFrame
# NOTE:两个🎲，两两独立
d = {(i,j):i+j for i in range(1,7) for j in range(1,7)}
dinv = defaultdict(list)
for i,j in d.items():
    dinv[j].append(i)
print(dinv[7])
x = {i:len(j)/36. for i,j in dinv.items()}
print(dinv.items())
print(x)
# NOTE:三个🎲，两两独立
d = {(i,j,k):(i*j*k)/2>(i+j+k) 
     for i in range(1,7) 
     for j in range(1,7) 
     for k in range(1,7)}
dinv = defaultdict(list)
for i,j in d.items():
    dinv[j].append(i)
print(dinv)
x = {i:len(j)/6**3. for i,j in dinv.items()}
print(x)
# NOTE:衍生四个🎲，两两独立
d = {(i,j,k,l):(i*j*k*l)/2>(i+j+k+l) 
     for i in range(1,7) 
     for j in range(1,7) 
     for k in range(1,7)
     for l in range(1,7)}
dinv = defaultdict(list)
for i,j in d.items():
    dinv[j].append(i)
print(dinv)
x = {i:len(j)/6**4. for i,j in dinv.items()}
print(x)
# NOTE:两个🎲，一个非公平
d = DataFrame(index=[(i,j) for i in range(1,7) for j in range(1,7)] ,
              columns=['sm','d1','d2','p1','p2','p'])
d['sm'] = list(map(sum,d.index))
d['d1'] = [i[0] for i in d.index]
d['d2'] = [i[1] for i in d.index]
d.loc[d['d1']<=3, 'p1'] = 1/9
d.loc[d['d1']>3, 'p1'] = 2/9
d['p2'] = 1/6
d['p'] = d['p1']*d['p2']
print(d.groupby('sm')['p'].sum())
# NOTE:衍生两个🎲，两个个非公平
d = DataFrame(index=[(i,j) for i in range(1,7) for j in range(1,7)] ,
              columns=['sm','d1','d2','p1','p2','p'])
d['sm'] = list(map(sum,d.index))
d['d1'] = [i[0] for i in d.index]
d['d2'] = [i[1] for i in d.index]
d.loc[d['d1']<=3, 'p1'] = 1/9
d.loc[d['d1']>3, 'p1'] = 2/9
d.loc[d['d2']<=3, 'p2'] = 1/3
d.loc[d['d2']>3, 'p2'] = 2/3
d['p'] = d['p1']*d['p2']
print(d.groupby('sm')['p'].sum())