import time
import threading
# 创建函数
def fun(n):
    for i in range(5):
        print(n,i)
        time.sleep(1)
# 创建两个线程
x = threading.Thread(target=fun,args=('第一次',))
x.start()
x1 = threading.Thread(target=fun,args=('第二次',))
x1.start()
# 加入join，待线程执行完后执行下一步
x1.join()
print('完成')