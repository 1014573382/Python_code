import json

data = {"id": 1, "name": "51test", "password":"88888"}
print(type(data))

# 将python数据类型转换为json数据类型
json_str = json.dumps(data)
print(type(json_str))
print(json_str)

# 将json数据类型转换为python数据类型
py_data = json.loads(json_str)
print(type(py_data))
print(py_data)
