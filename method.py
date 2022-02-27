class Human:
    cls_v="class variable"

    def __init__(self,name):
        self.name=name


    def show_name(self):
        print(self.name)
        print(self.cls_v)

    @classmethod
    def cls_method(cls, name):
        print(name)
        print(cls.cls_v)

    @staticmethod
    def emnite():
        print("nayamayt")

Human.human.cls_method()
print(Human.cls_v)
human=Human("nobita")
human.show_name()
Human.cls_method("Humaira")
human.emnite()
Human.emnite()