list1 = ['2', '5', '4', '3']
print(list1)
list1.sort()
print(list1)


def list_sort(list):
    a = "".join(list)
    sort_lista = sorted(a)
    # print(a)
    # print(sort_a)
    result = ''.join(sort_lista)
    print(result)

# for i in range(len(list)):
#     a = a + list[i]
# lis = a.split()
# lis.sort()
# print(lis)



found = {'a': 2, 'i': 3, 'e': 1 }

# for k in sorted(found):
#      print(k, 'was found', found[k], 'time(s).')

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times.')


if __name__ == '__main__':
    list1 = ['234', '523', '478', '693']
    list_sort(list1)