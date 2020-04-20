#Python Program to Create a Class and Compute the Area and the Perimeter of the Circle
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*(radius**2)

radius = int(input("Enter the radius of circle"))
obj = Circle(radius)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))