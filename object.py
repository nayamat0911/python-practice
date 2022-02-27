class Carton:
    series="tv series"
    def __init__(hey,name,age):
        hey.name=name
        hey.age=age
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)




obj = Carton("doremon",30)
obj2=Carton("shunchan",15)
obj3=Carton("nobita",35)
obj.age=40
obj2.name="jamal"
del obj2
obj.show()
obj2.show()
obj3.show()







