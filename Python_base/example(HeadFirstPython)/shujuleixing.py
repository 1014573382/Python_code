list = ['abcd',786 , 2.23 , 'runoob' , 70.2 ]
tinylist = [123 , 'runoob']

print(list)
print(list[0])
print(list[1:4])
print(list[2:])
print(tinylist[1])
print(tinylist + list)

print("---------------------------------------------")

list[0] = 222
list[3:5] = []
print(list)

print("---------------------------------------------")

letter = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
print(letter[1:7:2])

print("---------------------------------------------")

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  #输出集合，重复的元素被自动去掉

#成员测试
if 'Rose' in student :
      print("Rose 在集合中")
else :
      print("Rose 不在集合中")

# set可以进行集合运算
a = set('abcdeabcder')
b = set('abcdeopk')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素
