# Пользователь вводит два числа. Программа выводит диапазон чисел на экран от первого до последнего (не включая в диапазон последнее),
# но есть условия:
# - первое вводимое число должно быть больше второго, иначе ничего не произойдет;
# - выводятся все числа, за исключением тех, которые кратны 5;
# - если в диапазоне встречаются числа 23 или 32, то вывод идет до этих чисел и прерывается.
a = int(input('Input first number: '))
b = int(input('Input second number: '))
if a < b:
    while a < b :
        if a%5!=0:
            print(a)
        if a == 23 or a== 32:
            break
        a+=1
