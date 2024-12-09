# function
def get_matrix(n, m, value):
    matrix = []
    for arg in n, m, value:  # проверка на значение <= 0
        if arg <= 0:
            return matrix

    for i in range(n):  # n - колличество строк
        matrix.append([])
        for j in range(m):  # m - колличество столбцов
            matrix[i].append(value)  # value - значения

    return matrix


result1 = get_matrix(-1, -3, 10)
result2 = get_matrix(3, 0, 8)
result3 = get_matrix(4, 2, 3)

print(result1)
print(result2)
print(result3)

