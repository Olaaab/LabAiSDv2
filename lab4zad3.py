def dziel_i_zwyciezaj(vector):
    if len(vector) == 0:
        raise ValueError("Wektor jest pusty")
    elif len(vector) == 1:
        return vector[0]


    mid = len(vector) // 2
    left_half = vector[:mid]
    right_half = vector[mid:]

    max1 = dziel_i_zwyciezaj(left_half)
    max2 = dziel_i_zwyciezaj(right_half)

    return max(max1, max2)

vector = [5, 9, 3, 1, 7, 2, 8, 6]
max_element = dziel_i_zwyciezaj(vector)
print("Największy element wektora:", max_element)
