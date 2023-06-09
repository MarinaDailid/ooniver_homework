#Напишите программу которая умеет
#создавать матрицу заданных размеров n и m
#выводить её на экран
#находить наибольшее и наименьшее значения
#сортировать по возрастанию и по убыванию матрицы
#если матрица квадратная (равное количество столбцов и строк), то говорит об этом
from random import randint
def create_and_return_matrix(rows_number, elements_in_rows):
    matrix = []
    for i in range(rows_number):
        matrix.append([0] * elements_in_rows)

    for i in range(rows_number):
       for j in range(elements_in_rows):
          matrix[i][j] = randint(10, 99)
    return matrix

def cool_print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()

my_matrix = create_and_return_matrix(3, 4)
print(my_matrix)
min1 = my_matrix[0][0]
max1 = my_matrix[0][0]
for x in range(len(my_matrix)):
    for y in range(len(my_matrix[x])):
        if my_matrix[x][y] < min1:
            min1 = my_matrix[x][y]
        if my_matrix[x][y] > max1:
            max1 = my_matrix[x][y]

print("Min:", min1)
print("Max:", max1)


for o in range(len(my_matrix) * len(my_matrix[0])):
    prev_x = 0
    prev_y = 0
    prev_value = my_matrix[0][0]
    for x in range(len(my_matrix)):
        for y in range(len(my_matrix[x])):
            if x == 0 and y == 0:
                continue
            if(my_matrix[x][y] < prev_value):
                my_matrix[prev_x][prev_y] = my_matrix[x][y]
                my_matrix[x][y] = prev_value
            prev_x = x
            prev_y = y
            prev_value = my_matrix[x][y]

print(my_matrix)

for o in range(len(my_matrix) * len(my_matrix[0])):
    prev_x = 0
    prev_y = 0
    prev_value = my_matrix[0][0]
    for x in range(len(my_matrix)):
        for y in range(len(my_matrix[x])):
            if x == 0 and y == 0:
                continue
            if(my_matrix[x][y] > prev_value):
                my_matrix[prev_x][prev_y] = my_matrix[x][y]
                my_matrix[x][y] = prev_value
            prev_x = x
            prev_y = y
            prev_value = my_matrix[x][y]

cool_print_matrix(my_matrix)
if len(my_matrix) == len(my_matrix[0]):
    print('матрица квадратная')
    