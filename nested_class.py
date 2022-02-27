class Robot:
    def __init__(self,name):
        self.name=name

    def show_name_info(self):
        print(self.name)
        print("robot class")

    class Human:
        def __init__(self,name):
            self.name=name
        def show_name(self):
            print(self.name)
            print("human class")

    class Robo:
        def __init__(self,name):
            self.name=name
        def show_robo(self):
            print(self.name)
            print("robo cls")

        class Himu:
            def __init__(self,name):
                self.name=name

            def show_himo(self):
                print(self.name)
                print("himo class")

            class kaku:
                def __init__(self, name):
                    self.name = name

                def show_kaku(self):
                    print(self.name)
                    print("Kako class")

class Akash(Robot.Robo):
    def __init__(self,name):
        self.name=name

    def show_akash(self):
        print(self.name)
        print("akash")

    class Homa:
        def __init__(self,name):
            self.name=name

        def show_homa(self):
            print(self.name)
            print("homa Class")


robot=Robot("somaiya")
human=robot.Human("hasan")
robo=robot.Robo("Robo")
himo=robot.Robo.Himu("himo")
kakoo=robot.Robo.Himu.kaku("KAKU")

huma=Akash("Akash")
human=Akash.Himu("himo")
humanw=Akash.Himu.kaku('kaku')
print("---Akash--cls")
#huma.show_name_info()
human.show_himo()
human.show_himo()
humanw.show_kaku()


# robot.show_name()
#
# print("---human cls---")
# human.show_name()
#
# print("---robo cls----")
# robo.show_robo()
#
# print("--himo cls--")
# himo.show_himo()
#
# print("---kaku cls----")
# kakoo.show_kaku()