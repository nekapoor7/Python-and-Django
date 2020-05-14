class Bird:
    def intro(self):
        print("Bird")
    def fly(self):
        print("Birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich Can't fly")

def func(obj):
    obj.intro()
    obj.fly()

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_Ostrich = Ostrich()

func(obj_bird)
func(obj_sparrow)
func(obj_Ostrich)

