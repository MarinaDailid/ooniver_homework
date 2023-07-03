class Rescuers:
    def rest(self):
        print('Я отдыхаю')

    def jump(self):
        print('Я умею прыгать!')

    def run(self):
        print('Я умею бегать!!')

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
    pass
class Gaechka(Mouse):
   pass

gaechka = Gaechka()
gaechka.jump()
gaechka.run()
gaechka.rest()
vzhika = Vzhika()
vzhika.fly()
vzhika.run()
vzhika.jump()
vzhika.rest()
rokki = Rokki()
rokki.rest()
rokki.run()
rokki.jump()
deil = Deil()
deil.run()
deil.jump()
deil.rest()
chip = Chip()
chip.rest()
chip.jump()
chip.run()
