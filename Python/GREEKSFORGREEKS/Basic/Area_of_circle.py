import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def Area(self):
        return math.pi*self.radius**2


radius = int(input("Enter the radius of circle"))
obj = Circle(radius)
print("Area of circle:", round(obj.Area(), 2))