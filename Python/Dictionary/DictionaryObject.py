"""Write a Python program to get a dictionary from an object's fields."""

class dictobj:

    def __init__(self):
        self.red = 1
        self.blue = 3
        self.green = 2

    def do_nothing(self):
        pass

test = dictobj()
print(test.__dict__)