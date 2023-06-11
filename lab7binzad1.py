def binary_search(Y, L):
    left = 0
    right = len(L) - 1

    while left <= right:
        mid = (left + right) // 2
        if L[mid] == Y:
            return mid
        elif L[mid] < Y:
            left = mid + 1
        else:
            right = mid - 1

    return -1


L = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Y = 8
result = binary_search(Y, L)
if result != -1:
    print("Element", Y, "znajduje się na indeksie", result)
else:
    print("Element", Y, "nie został znaleziony w liście.")
