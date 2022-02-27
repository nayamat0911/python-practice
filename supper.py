class Robot:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

class Human():
    def __init__(self,name,age,food):
        # super().__init__(name,age)
        self.name=name
        self.age=age
        self.food=food
    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_food(self):
        print(self.food)

class Animal(Robot,Human):
    def __init__(self,name,age,food,pet):
        Human.__init__(self,name,age,food)
        Robot.__init__(self,name,age)
        self.pet=pet
    def show_pet(self):
        print(self.pet)

robot=Robot("somaiya","39 Years")
human=Human("hasan","23 years","Apple")
animal=Animal("nayamt","25 years","Mango","Cat")

print("---robot----")
robot.show_name()
robot.show_age()
print("---human----")
human.show_name()
human.show_age()
human.show_food()
print("----animal---")
animal.show_name()
animal.show_age()
animal.show_food()
animal.show_pet()
