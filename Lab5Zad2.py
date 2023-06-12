n = 6
lista = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            lista[i][j] = 0
        elif i == 0:
            lista[i][j] = 1
        elif j == 0:
            lista[i][j] = 0
        else:
            lista[i][j] = (lista[i - 1][j] + lista[i][j - 1]) / 2

for row in lista:
    print('     '.join([str(elem) for elem in row]))

print(lista)
