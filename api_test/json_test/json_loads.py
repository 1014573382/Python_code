import json

json_str = '{"id": 1, "name": "guonian", "password": "888888"}'
print(type(json_str))

# 将json数据类型转换为python数据类型
py_data = json.loads(json_str)
print(type(py_data))
print(py_data)
print(py_data['name'])

# 将python数据转化为json数据写入到文件
with open('./data.json', 'w')as f:
    json.dump(py_data, f)

# 从json文件读取数据转换为python数据类型
with open('data.json', 'r')as f:
    data = json.load(f)
    print(data)
    print(data['password'])