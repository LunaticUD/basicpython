# Time库
import time

# # TODO:时间获取：time() ctime() gmtime()TODO:
# print(time.ctime())  # Wed Jul 13 12:52:05 2022  当前时间
# print(time.time())  # 1657688062.7612474        时间戳
# print(time.gmtime())        # time.struct_time(tm_year=2022, tm_mon=7, tm_mday=13, tm_hour=4, tm_min=58, tm_sec=27,
# # tm_wday=2, tm_yday=194, tm_isdst=0)
# t = time.gmtime()
# print(time.strftime("%Y", t))
# # 时间格式化：strftime() strptime()
# # strptime(str, tpl)str是字符串形式的时间值
# a = '2018-01-26 12:55:20'
# t = time.strptime(a, "%Y-%m-%d %H:%M:%S")
# print(time.strftime("%Y-%m-%d %H:%M:%S", t))  # 2018-01-26 12:55:20
# 程序计时：sleep(), perf_counter()时间获取
# 测量时间：perf_counter()
# # TODO:产生时间：sleep()TODO:
# start = time.perf_counter()
# time.sleep(10)
# end = time.perf_counter()
# print(end - start)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))