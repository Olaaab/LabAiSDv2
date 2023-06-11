def suma(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]


    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]


    sum1 = suma(left_half)
    sum2 = suma(right_half)


    total_sum = sum1 + sum2


    return total_sum


array = [15, 5, 64, 8, 12, 11, 4, 35]
sum_of_elements = suma(array)
print("Suma elementów w tablicy:", sum_of_elements)
