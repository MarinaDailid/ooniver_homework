from random import randint

# worked_list = []
n = 100 # максимальный ӕлемент
quantity = 10 # количество ӕлементов списка
worked_list = [0] * quantity # создание списка заполненного ноликами

# изменение каждого нолика в списке на случайное число
for i in range(quantity):
    worked_list[i] = randint(0,n)
print(worked_list)
# Используйте сгенерированный список из первой задачи.
# Отсортируйте элементы в списке по возрастанию и выведите их в консоль.
worked_list.sort()
print(worked_list)