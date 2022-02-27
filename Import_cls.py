# from first_modul import Robot as r
# from first_modul import Human as h
import first_modul as f
from second_modiul import Animal

robot=f.Robot("Hasan","34 years old")
human=f.Human("shinchan","30 years old", "aple")
animal=Animal("nayamat","25 years old","Apple","Cat")


robot.show_name()
robot.show_age()

print("----human----")
human.show_name()
human.show_age()
human.show_food()

print("---animal----")
animal.show_name()
animal.show_age()
animal.show_food()
animal.show_pet()