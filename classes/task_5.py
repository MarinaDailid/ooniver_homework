class Rescuers:
    __weight: float = 0
    height: int = 0
    __fatigue: int = 0

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight = 0.01):
        self.__weight += min(0.05, weight) # не больше 0.05

    @property
    def fatigue(self):
        return self.__fatigue

    @fatigue.setter
    def fatigue(self, fatigue):
        self.__fatigue = fatigue
        if self.__fatigue > 10:
            print(f'[{self.__class__.__name__}] Я устал ')
            self.rest()


    def run(self):
        self.fatigue += 1
        print(f'[{self.__class__.__name__}] Я умею бегать!!')
    def jump(self):
        self.fatigue += 1
        print(f'[{self.__class__.__name__}] Я умею прыгать!')
    def fly(self):
        self.fatigue += 1
        print(f'[{self.__class__.__name__}] Я умею летать!')
    def rest(self):
        self.__fatigue = 0
        print(f'[{self.__class__.__name__}] Я отдыхаю')


class Mouse(Rescuers):
    pass

class Chipmunk(Rescuers):
    pass

class Fly(Rescuers):
    def fly(self):
        print('Я умею летать!')

class Chip(Chipmunk):
    pass

class Deil(Chipmunk):
    pass
class Rokki(Mouse):
   pass
class Vzhika(Fly):
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight=0.001):
        self.__weight += 0.001
        if self.__weight > 0.02:
            print('Вжик не летает пока не похудеет')

class Gaechka(Mouse):
   pass


gaechka = Gaechka()
gaechka.jump()
vzhika = Vzhika()
for i in range(11):
    vzhika.fly()

rokki = Rokki()
rokki.rest()
deil = Deil()
deil.run()
chip = Chip()
chip.rest()


