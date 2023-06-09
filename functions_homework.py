#cоздайте функцию которая принимает в качестве аргументов название машин (марка машины) и  год выпуска,
# печатает их в одной строке,  например вот так: `Отличная Mazda 2003 года`.
# Создайте список из 5 словарей которые будут использованы для проброса параметров в функции.
#Вызовите функцию для каждого элемента в списке.

def cars(car, year):
    message = f'отличная {car} {year} года'
    print(message)

my_cars = [
    {'car': 'opel', 'year': 2001},
    {'car': 'lexus', 'year': 2022},
    {'car': 'audi', 'year': 2012},
    {'car': 'bugatti', 'year': 2022},
    {'car': 'bmw', 'year': 2023},
]

for i in my_cars:
    cars(i['car'], i['year'])

def ymnozit(a,b):
    return a + b

res = ymnozit(2, 3)
print(res)