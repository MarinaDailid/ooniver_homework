#Создаем функцию которая принимает на вход неопределенное количество аргументов
# и возвращает сумму элемента умноженного на его индекс
#например: (2, 5, 6, 7) -> 2 * 0 + 5 * 1 + 6 * 2 + 7 * 3
def summm(*args):
    s = 0
    for i in range(len(args)):
        s += args[i] * i
    return s
s = summm(1, 2, 3, 4)
print(s)
