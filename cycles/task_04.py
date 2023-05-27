#Напишите программу которая выводит все Простые числа
# (числа, которые делятся только на себя и на 1) в диапазоне от 0 до 100.
a = range(0, 100)
for b in a:
    if b<2:
        continue
    c = range(2, b)
    simple = True
    for D in c:
        if b%D==0:
            simple = False
            break

    if simple == True:
        print(b)
