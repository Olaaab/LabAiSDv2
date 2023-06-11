def remove(lst, i):
    if i < 1 or i > len(lst):
        print("Nieprawidłowy indeks węzła.")
        return

    lst.pop(i - 1)

my_list = [5, 'cat', 9]
i = 2
print("Przed usunięciem:", my_list)
remove(my_list, i)
print("Po usunięciu:", my_list)
