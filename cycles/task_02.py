# У вас есть следующий список [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] .
# Напишите программу которая переберет все элементы и запишет каждый четный элемент два раза рядом,
# каждый нечетный возведет в степень самого себя и выведет на экран.
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for a in my_list:
    if a%2==0:
        print(a, a)
    else:
        print(a**a)