def summa(a, b, c):
   s = a + b + c
   return s # Для того, что бы увидеть результат

def summa_2(a1, a2, a3):
    s = a1+ a2 +a3
    print(s)

def main():
    sss = summa(1, 7, 8)
    print(sss)
    summa_2(21, 2, 3) # вызываем функцию (для того, что бы она выполнилась)

if __name__ == '__main__':
    main()

def print_car(name, year):
    print(f'Отличная {name} {year} года')


car_1={'mazda': 2004}
car_2={'opel': 2003}
car_3={'lamba': 2054}
car_4={'mers': 2024}
car_5={'mazda': 2011}
car_list =[car_1, car_2, car_3, car_4, car_5]
for car in car_list:
    for key, value in car.items():
        print_car(key, value)
