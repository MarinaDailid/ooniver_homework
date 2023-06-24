
from random import randint


def create_matrix(n, m): # создание матрицы с 11 по 18 строки
    rows = []  # строки
    matrix = []  # матрица
    for j in range(n):
        for i in range(m):
            rows.append(randint(0, 9))
        matrix.append(rows)
        rows = []
    return matrix

def print_matrix(matrix): # вместо пасс вставить функцию
    pass

if __name__ == '__main__':
    matrix_1 = create_matrix(3, 4)
    print_matrix(matrix_1)
    print(matrix_1)

# взять стороку и перенеси ӕнд, добавить новый принт (для принта матрицы)
