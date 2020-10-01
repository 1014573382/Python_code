import xlrd
import csv
import os
import json

excel_name = r"D:\新网银行\excel_to_csv\新网银行票据业务平台接口V1.6.xlsx"

workbook = xlrd.open_workbook(excel_name,encoding_override="utf-8")
tables_num = workbook.nsheets  # 获取sheet数

api_name_cn = []
api_name_en = []
request_field = []

for num in range(2,tables_num):
    table = workbook.sheet_by_index(num)
    apiname_cn = table.cell_value(0, 0)  # 第一个单元格的值
    apiname_en = table.cell_value(1, 1)
    api_name_cn.append(apiname_cn)  # 获取每一个sheet的第一行第一列值（中文接口名）存入列表
    api_name_en.append(apiname_en)  # 获取每一个sheet的第二行第二列值（英文接口名）存入列表

    # 获取所有的请求参数（获取第三列的内容，并进行截取）
    all_field = table.col_values(2)
    # print(all_field)
    all_request_field = all_field[6:]
    # print(all_request_field)
    # print(all_request_field.index('英文名称'))
    request_end_index = all_request_field.index('英文名称')
    only_request_field = all_request_field[0:request_end_index-1]
    # print(only_request_field)
    request_field.append(only_request_field)

print(request_field)
print(len(request_field))

dict_request = {}
for i in range(len(request_field)):
    for j in request_field:
        dict_request[request_field[i[j]]] = ""

# print(dict_request)



# dict_request = {}
# for i in request_field:
#     for j in range(len(i)):
#         dict_request[i[j]] = ''
# print(dict_request)
# json_request = json.dumps(request_field, ensure_ascii=False)


# str_json_request = json.dumps(request_field,indent=2, ensure_ascii=False)
# print(str_json_request)

# print(api_name_en)
# print(api_name_cn)
# print(request_field)


