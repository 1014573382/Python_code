name = 'linlin'
age = 32
gender = 'male'
list1 = [1,2,3,6]
dict1 = {'name': 'guoguo', 'age': 25}

# print('my name is %s, my age is %d.' %(name,age))

# 通过string.format()方法拼接
print('my list is {}, my dict is {}'.format(list1,dict1))
print('my name is {0}, my age is {1},{1} {0} {1}'.format(name,age))

namelist = ['Tom', 'Jarry','Sam']
print('names:{}、{} and {}'.format(*namelist))
print('My name is {name}, my age is {age}'.format(**dict1))

# Formatted string literals，字符串格式化机制
print(f"my name is {name}, my age is {age},my list is {namelist},my dict is dict {dict1}")
print(f"my name is {name}, my age is {age},my list is {namelist[0]},my dict is dict {dict1['name']}")

print(f"my name is {name.upper()}")
print(f'result is { (lambda x: x*2)(4) }')

