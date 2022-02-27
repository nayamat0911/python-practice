class Nobita:
    def __init__(self):
        self.book="comics"
        self.no=30
        self._no=40
        self.__no=50

    def show(self):
        print(self.no,self._no,self.__no)


class Sonio(Nobita):
    def show_nobita(self):
        print("sonio",self.no)

class Shijuka(Nobita):
    def show_nobita_info(self):
        print("shijuka",self._no,self.__no)

nobita=Nobita()
sonio=Sonio()
sijuka=Shijuka()
nobita.show()
sonio.show_nobita()
sijuka.show_nobita_info()