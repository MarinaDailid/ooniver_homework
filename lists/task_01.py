from random import randint

# worked_list = []
n = 100 # максимальный ӕлемент
quantity = 10 # количество ӕлементов списка
worked_list = [0] * quantity # создание списка заполненного ноликами

# изменение каждого нолика в списке на случайное число
for i in range(quantity):
    worked_list[i] = randint(0,n)
print(worked_list)

# Выведите в консоль все четные элементы списка и элементы которые закачиваются цифрой 7.
for a in worked_list:
    if a % 2 == 0 or a % 10 == 7:
        print(a)
#Выведите максимальный и минимальный элементы списка используя только логические операции сравнения.
min1 = 999
max1 = 0
for a in worked_list:
    if a < min1:
        min1 = a
    if a > max1:
        max1 = a

print("Min:", min1)
print("Max:", max1)

min2 = min(worked_list)
max2 = max(worked_list)
print("Min:", min2)
print("Max:", max2)