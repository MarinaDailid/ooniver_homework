class Person:
    name: str
    age: int
    weight: int

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def say_hello(self):
        print('Hello ')


person_alex = Person('Alex', 26, 70)
person_alex.say_hello()
print(person_alex.name)
person_marina = Person('Marina', 25, 90)
