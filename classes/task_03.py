class Person:
    name: str
    height: int
    __age: int
    weight: int
    __salary: int

    def __init__(self, name, height, age, weight, salary = 1000):
        self.name = name
        self.__age = age
        self.weight = weight
        self.height = height
        self.__salary = salary

    def incr_age(self):
        self.__age += 1

    def birthday(self):
        self.incr_age()
        print(f'С днем рождения! Теперь тебе {self.__age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print('Ошибка, неверный возраст')

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary


person_alex = Person('Alex', 180, 26, 70, 1000)
person_alex.birthday()
person_alex.salary = 20000
print(f'Моя ЗП = {person_alex.salary}$')