from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def go_school(self):
        pass

    #concret method
    def result(self):
        print("ka")

    @abstractmethod
    def go_collage(self):
        pass

class Nobita(Father):
    def go_school(self):
        print("Ha gesilam")
    def playing(self):
        print("Playing footbal")
    def go_collage(self):
        print("hello")

    def singing(self):
        print("Singing")


nobita=Nobita()
nobita.result()
nobita.go_school()
nobita.playing()
nobita.singing()
nobita.go_collage()

