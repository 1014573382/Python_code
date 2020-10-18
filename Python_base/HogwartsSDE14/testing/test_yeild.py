#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/14 21:52

# yeild 生成器
def fun():
    for i in range(3):
        print(f"i = {i}")
        yield   #相当于return  同时相当于暂停并且记住 上一次的执行位置
        print('end')

f =fun()
next(f)
next(f)
next(f)
