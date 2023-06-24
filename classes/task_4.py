class Rescuers:
    def run(self):
        print('Я умею бегать!!')
    def jump(self):
        print('Я умею прыгать!')
    def fly(self):
        print('Я умею летать!')
    def rest(self):
        print('Я отдыхаю')


class Chip(Rescuers):
    pass
class Deil(Rescuers):
    pass
class Rokki(Rescuers):
    pass
class Vzhika(Rescuers):
    pass
class Gaechka(Rescuers):
    pass

gaechka = Gaechka()
gaechka.jump()
vzhika = Vzhika()
vzhika.fly()
rokki = Rokki()
rokki.rest()
deil = Deil()
deil.run()
chip = Chip()
chip.rest()


