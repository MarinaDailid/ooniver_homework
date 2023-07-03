class Person:
    name: str
    age: int
    weight: int
    sleep: bool

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def say_hello(self, name):
        print('Hello ' + name)


person_alex = Person('Alex', 26, 70)
person_alex.say_hello('Barsik')
print(person_alex.name)
person_marina = Person('Marina', 25, 90)
