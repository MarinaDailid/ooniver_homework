#измените в вашей программе функцию, которая создает матрицу таким образом,
# чтобы если второй параметр, который `m`, не указан при вызове,
# то на его место встанет случайное число от 1 до 9 включительно.
#Напишите программу, которая считает факториал для числа n.
#например: факториал 5, это 5 * 4 * 3 * 2 * 1
from random import randint
def create_and_return_matrix(n, m = 0):
    if m ==0:
        m = randint(1, 10)
    matrix = []
    for i in range(n):
        matrix.append([0] * m)

    for i in range(n):
       for j in range(m):
          matrix[i][j] = randint(10, 99)
    return matrix
print(create_and_return_matrix(3))

def factorial(n):
    f = n
    for i in range(1, n):
        f *= i
    return f

f = factorial(5)
print(f)
