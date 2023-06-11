def fibonacci(n):
    fib_table = [0, 1]

    if n <= 1:
        return fib_table[n]

    for i in range(2, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]


n = 11
result = fibonacci(n)
print(f"Element o indeksie {n} w ciągu Fibonacciego: {result}")