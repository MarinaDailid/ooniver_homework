from random import randint

#По аналогии с первой задачей сгенерируйте квадратную матрицу из 9 элементов (3 на 3 элемента). Если сложно, напишите  ее руками =) но цифры в ней должны быть различны и не упорядочены изначально.
#Ваша задача найти максимальный и минимальный элементы в матрице.

s = 3
m = [
#    0  1  2
    [0, 1, 2], # 0
    [0, 1, 2], # 1
    [0, 1, 2], # 2
]

for x in range(s):
    for y in range(s):
        m[x][y] = randint(0, 20)
print(m)

min1 = 999
max1 = 0
for x in range(s):
    for y in range(s):
        if m[x][y] < min1:
            min1 = m[x][y]
        if m[x][y] > max1:
            max1 = m[x][y]

print("Min:", min1)
print("Max:", max1)