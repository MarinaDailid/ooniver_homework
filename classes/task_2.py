class Person:
    name: str
    height: int
    age: int
    weight: int

    def __init__(self, name, height, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


    def incr_age(self):
        self.age += 1

    def birhday(self):
        self.incr_age()
        print(f'С днем рождения! Теперь тебе {self.age}')

person_alex = Person('Alex', 180, 26, 70)
print(person_alex.age)
person_alex.incr_age()
print(person_alex.age)
person_alex.birhday()
