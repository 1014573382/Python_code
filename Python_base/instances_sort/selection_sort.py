# coding=utf-8


def select_s(data):
    # 第一层循环，取出数组中的每个元素
    for i in range(len(data) - 1):
        temp = i   # 拿取第一个元素用来比较
        # 第二层循环，从i后面的第一个值开始循环，玉data[i]进行比较
        for j in range(i+1, len(data)):
            if data[j] < data[temp]:
                data[temp], data[j] = data[j], data[temp]
    print(data)


if __name__ == '__main__':
    data = [14, 31, 14, 6, 18, 24, 2, 40]
    select_s(data)