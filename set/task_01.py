#Сгенирируйте список из ста случайных элементов элементов (от 10 до 99).
# Выведите только уникальные из них.
from random import randint
list = [0]*100
for a in range(0, 100):
    b = randint(10, 99)
    list[a] = b
print(list)
list_01 = set(list)
print(list_01)
