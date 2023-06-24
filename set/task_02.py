#Сгенирируйте два списка  по 10 случайных элементов (от 0 до 9).
# Найдите элементы которые входят только в первый список, только во второй,
# только общие элементы и только различные.
from random import randint
list_01 = [0]*10
for a in range(0, 10):
    b = randint(0, 9)
    list_01[a] = b
print(list_01)
list_02 = [0]*10
for a in range(0, 10):
    b = randint(0, 9)
    list_02[a] = b
print(list_02)
intersection_list = set(list_01).intersection(list_02) # одновременно в 2 множествах
print(intersection_list)
difference_list = set(list_01).difference(list_02) # есть в 1 множестве, но нет во 2
print(difference_list)
difference_list2 = set(list_02).difference(list_01) # есть в 2 множестве, но нет во 1
print(difference_list2)
intersection_list_2 = set(list_02).intersection(list_01) # одновременно в 2 множествах
print(intersection_list_2)
intersection_list_3 = set(list_01).symmetric_difference(list_02) # только разные значения
print(intersection_list_3)
