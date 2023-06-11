def add_sorted(lst, value):
    i = 0
    while i < len(lst) and value > lst[i]:
        i += 1
    lst.insert(i, value)

# Przykład użycia
my_list = [2, 4, 6, 8, 10, 12]
print("Przed dodaniem:", my_list)
add_sorted(my_list, 5)
print("Po dodaniu:", my_list)
add_sorted(my_list, 3)
print("Po dodaniu:", my_list)
add_sorted(my_list, 9)
print("Po dodaniu:", my_list)
