#Сгенирируйте два списка различной длинны(до 20 элементов максимальный список).
#Сделайте из них словарь, чтобы ключами для словаря были значения большего из списков,
# а значениями для словаря — значения из меньшего списка деленные на 2. Выведите словарь в консоль.
from random import randint
list_01_len = randint(1, 20)
list_01 = [0] * list_01_len
for a in range(0, list_01_len):
    list_01[a] = randint(1, 20)
print(list_01)
list_02_len = randint(1, 20)
list_02 = [0] * list_02_len
for a in range(0, list_02_len):
    list_02[a] = randint(1, 20)
print(list_02)

dict_01 = {}
if len(list_01) > len(list_02):
    keys = list_01
    values = list_02
else:
    keys = list_02
    values = list_01

for i in range(len(keys)):
    if i < len(values):
        dict_01[keys[i]] = values[i]/2
    else:
        dict_01[keys[i]] = 0
print(dict_01)
