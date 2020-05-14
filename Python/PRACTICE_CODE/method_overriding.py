class Bird:
    def intro(self):
        print("Birds")
    def fly(self):
        print("Birds can Fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def fly(self):
        print("Sparrow cant fly")

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.intro()
obj_bird.fly()

obj_sparrow.intro()
obj_sparrow.fly()

obj_ostrich.intro()
obj_ostrich.fly()
