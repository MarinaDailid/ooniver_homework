from abc import ABC, abstractmethod


class Rescuers(ABC):
    @abstractmethod
    def run(self):
        pass


class Chipmunk(Rescuers):
    def run(self):
        print('Я умею бегать')


chip = Chipmunk()
chip.run()
