#Программа просит ввести число. Если оно меньше 0, говорит что оно отрицательное,
#если больше 0 — положительно,
#если равно 0 — говорит что оно равно 0 =)
a = (input('Введите число: '))
b = int(a)
if b < 0:
    print('число отрицательное')
elif b > 0:
    print('число положительное')
else:
    print('число равно нулю')