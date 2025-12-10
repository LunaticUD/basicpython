# 循环
# for...in...
k = 0
for i in range(1,101):
    k = i +k
print(k)
# while
a = b = 1
while True:
    b += 1
    a += b
    if b == 100:
        break
print(a)
# break
# 终结掉整个循环
# continue
# 结束掉本次循环