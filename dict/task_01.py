#cоздайте словарь с 10-тью ключами, в котором ключами будут случайные числа от 10 до 99 включительно,
# а значениями эти же числа, но возведенные в куб. Выведите словарь в консоль.
# Удалите ключи, значение для которых кратны 2. Опять выведите на экран.
# Из получившегося словаря сделайте два списка, один с ключами — второй со значениями.
# Отсортируйте их по убыванию (не используйте встроенные методы сортировки). Выведите списки на экран.
from random import randint
dict = {}
for a in range(0,10):
    b = randint(10, 99)
    dict[b] = b**3
print(dict)
for key in list(dict.keys()):
    if key % 2 == 0:
        del dict[key]
print(dict)
list_keys = list(dict.keys())
list_values = list(dict.values())
sorted_keys = []
while len(list_keys) > 0:
    a = max(list_keys)
    list_keys.remove(a)
    sorted_keys.append(a)
print(sorted_keys)
sorted_values = []
while len(list_values) > 0:
    b = max(list_values)
    list_values.remove(b)
    sorted_values.append(b)
print(sorted_values)