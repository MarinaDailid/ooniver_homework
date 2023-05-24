#Сгенирируйте два списка  по 10 случайных элементов (от 0 до 9).
# Найдите элементы которые входят только в первый список, только во второй,
# только общие элементы и только различные.
from random import randint
list_01 = [0]*10
for a in range(0,10):
    b = randint(0, 9)
    list_01[a] = b
print(list_01)
list_02 = [0]*10
for a in range(0,10):
    b = randint(0, 9)
    list_02[a] = b
print(list_02)