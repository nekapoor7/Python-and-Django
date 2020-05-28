"""Write a Python program to get a dictionary from an object's fields."""

class Dict:

    def __init__(self):
        self.red = 1
        self.green = 2
        self.black = 3
        self.pink = 4
        self.purple = 5

    def print(self):
        pass

d = Dict()
print(d.__dict__)