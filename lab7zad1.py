def search_value(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1


my_list = [4, 'cat', 8.4]
value = 'cat'
index = search_value(my_list, value)
if index != -1:
    print(f'Wartość {value} została znaleziona na pozycji {index}.')
else:
    print(f'Wartość {value} nie została znaleziona na liście.')
