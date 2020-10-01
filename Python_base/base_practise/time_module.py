#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/01 20:47
import time

# time.strftime() 将当前的时间戳转成带格式的时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# time.localtime() 时间戳转成时间元祖
print(time.localtime())

# 时间戳
print(time.time())
print(int(time.time()))
# time.asctime() 国外的时间格式
print(time.asctime())

# 获取两天前的时间
now_timestamp = time.time()
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
two_day_before = now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))
