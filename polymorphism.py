class Robot:
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print(self.name)
        print("Robot Cls")

class Human(Robot):
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print(self.name)
        print("Human cls")

robot=Robot("Robotics")
human=Human("humuinity")

robot.show_name()
human.show_name()
# print("poly-------------------")
# for i in (human, robot):
#     i.show_name()

class Profile:
    def name(self,first=None,middle=None,last=None):
        if first !=None and middle !=None and last !=None:
            print(first+" "+middle+" "+last)
        elif first !=None and middle !=None:
            print(first+" "+middle)
        else:
            print(first)
p=Profile()
p.name("marjuk","ahmed","siddik")