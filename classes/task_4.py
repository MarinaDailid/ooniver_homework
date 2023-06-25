class Rescuers:
    def rest(self):
        print('Я отдыхаю')

    def jump(self):
        print('Я умею прыгать!')

    def run(self):
        print('Я умею бегать!!')
class Chip(Rescuers):
    pass

class Deil(Rescuers):
    pass
class Rokki(Rescuers):
   pass
class Vzhika(Rescuers):
    def fly(self):
        print('Я умею летать!')

    def run(self):
        print('Я не умею бегать!!')
class Gaechka(Rescuers):
   pass

gaechka = Gaechka()
gaechka.jump()
vzhika = Vzhika()
vzhika.fly()
vzhika.run()
rokki = Rokki()
rokki.rest()
deil = Deil()
deil.run()
chip = Chip()
chip.rest()


