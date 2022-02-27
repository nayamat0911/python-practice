class Doremon:
    def doremon_self(self):
        print("I am doremon doremon ")
    def gadeget(self):
        print("new gadeget")

class Nobita:
    def nobita_calls(self):
        print("i am nobita class")

class Shijuka(Doremon,Nobita):
    def sijuka_als(self):
        print("i am shijuka")

doremon=Doremon()
nobita=Nobita()
shijuka=Shijuka()



shijuka.sijuka_als()
shijuka.doremon_self()
shijuka.nobita_calls()