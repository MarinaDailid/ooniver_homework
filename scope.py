#goal_1 = 'mitsubishi'
#goal_2 = 'mersedes'
#name = 'Misha'
#def print_first_goal():
  #  name = 'Anna'
 #   print(f'{name} want to buy a car - {goal_1}')
#def print_second_goal():
  #  name = 'Misha'
 #   print(f'{name} want to buy a car - {goal_2}')
#print_first_goal()
#print_second_goal()


#def print_first_goal():
 #   goal_1 = 'mitsubisi'
  #  name = 'Alex'
   # print(f'{name} want to buy a car - {goal_1}')
#print_first_goal()
#def second_goal():
   # goal_2 = 'mers'
  #  name = 'Oleg'
 #   print(f'{name} want to buy a car - {goal_2}')
#second_goal()

#goal_1 = 'mitsubishi'
#goal_2 = 'mersedes'
#name = 'Misha'
#def print_first_goal():
    #global name
    #name = 'Anna'
    #print(f'{name} want to buy a car - {goal_1}')
#def print_second_goal():
    #print(f'{name} want to buy a car - {goal_2}')
#print_first_goal()
#print_second_goal()

def print_first_goal():
    goal_1 = 'mitsubishi'
    name = 'Anna'
    print(f'{name} want to buy a car - {goal_1}')
    def print_name():
        nonlocal name
        name = 'Sergey'
        print(f'{name} !!!')
    print_name()
    print(name)


print_first_goal()

#Создаем функцию которая принимает на вход неопределенное количество аргументов
# и возвращает сумму только тех, которые кратны 3
def sum(*args):
    s = 0
    for elem in args:
        if elem % 3 == 0:
            s += elem

    return s

s = sum(1, 4, 7, 78, 9)
print(s)

#создайте функцию которая принимает на вход неопределенное количество именованных аргументов
# и печатает в консоль только те, значения которых кратны 5

def age_summ(**kwargs):
    s = 0
    for key, value in kwargs.items():
        if key.startswith('A'):
            if value % 5 == 0:
                s += value
    return s
s = age_summ( A= 10, B = 16, Al = 2)
print(s)

#Напишите программу которая умеет создавать матрицу заданных размеров n и m
#выводить её на экран
#находить наибольшее и наименьшее значения
#сортировать по возрастанию и по убыванию матрицы
#если матрица квадратная (равное количество столбцов и строк), то говорит об этом
from random import randint
row_numbers = 4
elements_in_rows = 5
matrix = []
for i in range(row_numbers):
    matrix.append([0] * elements_in_rows)
print(matrix)
#def matix(n,m):
 #   n= 4
  # for i in range(row_numbers):
   # matrix.append([0] * elements_in_rows)
    #matr(4 ,5)
#print(matr)
def create_matrix(row_numbers,elements_in_rows):
    matrix = []
    for i in range(row_numbers):
        matrix.append([0] * elements_in_rows)

        for j in range(elements_in_rows):
            matrix[i][j] = randint(10, 99)
        return matrix

def cool_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end= ' ')
        print()
my_matrix = create_matrix(3, 4)
print(my_matrix)

