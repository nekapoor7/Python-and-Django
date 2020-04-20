# Python program to show that the variables with a value
# assigned in class declaration, are class variables

class Student:

    stream = 'cse'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# Objects of Student class

a = Student ('Neha',24)
b = Student ('Harsh',19)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

# Class variables can be accessed using class
# name also

print(Student.stream)