import xlrd
import csv
import os

#生成的csv文件名
# csv_file_name = 'excel_to_csv.csv'

def get_excel_list():
    # 获取Excel文件列表
    excel_file_list = []
    # file_list = os.listdir(os.getcwd())
    file_list = os.listdir(r"D:\新网银行\excel_to_csv")
    for file_name in file_list:
        if file_name.endswith('xlsx') or file_name.endswith('xls'):
            excel_file_list.append(file_name)
    return excel_file_list


def excel_read(excel_name):
    # 读取Excel文件中的中文接口名
    workbook = xlrd.open_workbook(excel_name,encoding_override="utf-8")
    tables_num = workbook.nsheets  # 获取sheet数
    api_name_cn = []
    api_name_en = []
    request_field = []
    for tablenum in range(2,tables_num):
        table = workbook.sheet_by_index(tablenum) #循环读取sheet
        # nrows = table.nrows
        # nclos = table.ncols
        apiname_cn = table.cell_value(0,0)  #第一个单元格的值
        apiname_en = table.cell_value(1,1)
        api_name_cn.append(apiname_cn)  # 获取每一个sheet的第一行第一列值（中文接口名）存入列表
        api_name_en.append(apiname_en)  # 获取每一个sheet的第二行第二列值（英文接口名）存入列表

        # 获取所有的请求参数（获取第三列的内容，并进行截取）
        all_field = table.col_values(2)
        all_request_field = all_field[6:]
        # 获取列表中"英文名称"所在位置的索引值
        request_end_index = all_request_field.index('英文名称')
        only_request_field = all_request_field[0:request_end_index-1]
        request_field.append(only_request_field)

    return api_name_cn,api_name_en,request_field

#
# def read_apiname_en(excel_name):
#     workbook = xlrd.open_workbook(excel_name, encoding_override='utf-8')
#     table_num = workbook.nsheets


def xlsx_to_csv(csv_file_name, row_value):
    # 生成CSV文件
    with open(csv_file_name, 'a', newline='')as f:
        write = csv.writer(f)
        write.writerow(row_value)

    # for rows_read in range(nrows):

if __name__ == '__main__':
    file_path = r"D:\新网银行\excel_to_csv"
    # 获取Excel列表
    excel_list = get_excel_list()
    # print(excel_list)
    for excel_name in excel_list:
        # 指定路径与文件名拼接
        # 生成的CSV文件
        csv_file_name = file_path + '\\' + excel_name + '.csv'
        # 对应路径下的excel文件
        excel_name_fin = file_path + '\\' + excel_name

        # 写入标题行
        csv_title = ['接口名_CN', '接口名_EN', '请求报文']
        xlsx_to_csv(csv_file_name, csv_title)

        print(excel_read(excel_name_fin))

        for row_value in excel_read(excel_name_fin):
            xlsx_to_csv(csv_file_name, [row_value])


