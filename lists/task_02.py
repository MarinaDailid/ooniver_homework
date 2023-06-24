#вторая задача по спискам, попробуй написать сортировку не используя встроеные методы.
# Сравнивай соседние элементы
from random import randint

# worked_list = []
n = 100 # максимальный ӕлемент
quantity = 10 # количество ӕлементов списка
worked_list = [0] * quantity # создание списка заполненного ноликами

# изменение каждого нолика в списке на случайное число
for i in range(quantity):
    worked_list[i] = randint(0, n)
print(worked_list)
# Используйте сгенерированный список из первой задачи.
# Отсортируйте элементы в списке по возрастанию и выведите их в консоль.
for o in range(quantity):
    for i in range(1, quantity):
        b = worked_list[i]
        a = worked_list[i-1]
        if a > b:
            worked_list[i] = a
            worked_list[i-1] = b

print(worked_list)
