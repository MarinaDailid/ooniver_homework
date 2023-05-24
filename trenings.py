#name = 'Привет мир!'
#for i in name:
   # print(i)

#name = 'Привет мир!'
#for i in range(1,11):
   # print(name)

#a = 1
#while a <= 10:
   # if a != 5:
    #    print(a)
    #a += 1
   # continue
# бесконечный цикл
#b = 1
#while b == 1:
  #  print('бесконечный цикл')

#a = input('Введите число: ')
#a = int(a)
#if a % 2 == 0:
#    print("число четное")
#a = input('Введите число: ')
#a = int(a)
#if a < 0:
 #   print('число отрицательное')
#elif a > 0:
 #   print('число положительное')
#else:
 #   print('число равно нулю')

#Создайте словарь с 10-тью ключами, в котором ключами будут случайные числа от 10 до 99 включительно,
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


#### func
def my_func(a, b, c):
    return a + b + c

asq = my_func(1, 2, 3)
