#Python Program to Find the Area of a Rectangle Using Classes

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return(self.length * self.breadth)

length = int(input("Enter the length"))
breadth = int(input("Enter the breadth"))
Area = length * breadth
print("Area of Rectangle",Area)
