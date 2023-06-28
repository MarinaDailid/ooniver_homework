try:
    a = int(input('a = '))
    b = int(input('b = '))
except ValueError:
    print('Вы ввели не число')
else:
    try:
        c = a / b
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
    else:
        print(c, 'Все прошло удачно')
finally:
    print('удачи')

try:
    c = int(input('a = ')) / int(input('b = '))
except (ZeroDivisionError, ValueError) as err_:
    print(f'У вас ошибка {err_}')





