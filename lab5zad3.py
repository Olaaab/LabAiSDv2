def oblicz_S(n):
    S_table = [1, 1]

    if n <= 1:
        return S_table[n]

    for i in range(2, n + 1):
        S_table.append(2 * S_table[i - 1] - S_table[i - 2])

    return S_table[n]


n = 5
result = oblicz_S(n)
print(f"Wartość {n}-tego wyrazu ciągu S(n): {result}")
