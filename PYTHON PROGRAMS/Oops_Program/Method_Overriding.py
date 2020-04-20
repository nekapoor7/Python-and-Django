class Bird:
    def intro(self):
        print("There are several types of bird")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")

obj_Bird = Bird()
obj_sparrow = sparrow()
obj_ostrich = ostrich()

obj_Bird.intro()
obj_Bird.flight()

obj_sparrow.intro()
obj_sparrow.flight()

obj_ostrich.intro()
obj_ostrich.flight()
