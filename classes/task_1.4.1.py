class Person:
    name: str
    age: int
    weight: int
    sleep: bool

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def go_sleep(self, hour):
        if hour >= 23 or hour < 7:
            self.sleep = True
            print('Я пошел спать')
        else:
            self.sleep = False
            print('Спать еще рано')

    def up(self, hour):
        if self.sleep == False:
            print('Я еще не сплю')
        elif 7 <= hour < 23 :
            self.sleep = False
            print('Я проснулся')


person_alex = Person('Alex', 26, 70)
person_alex.go_sleep(12)
print(person_alex.sleep)
person_marina = Person('Marina', 25, 90)
person_alex.up(8)

