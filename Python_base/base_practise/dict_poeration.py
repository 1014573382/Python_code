import sys
# 两种定义字典的方式
found = {'login': True, 'username': 'guoxl','passwd': '88888'}
a = dict(a=1, b=2)

# 返回被删除的末尾键值对
print(found.popitem())
print(found)

c = {}
d = c.fromkeys((1,2,3),"a")
print(d)

print({i: i*2 for i in range(1,4)})

# 查看当前模块定义的对象
print(dir())

print(dir(sys))