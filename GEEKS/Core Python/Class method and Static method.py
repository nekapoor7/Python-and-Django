"""Class Method and Static Method

1. Class Method : A class method is a method which is bound to the class and not to the object of the class.
A class method receives the class as implicit first argument. they have access to the state of the class as it
takes a class parameter that points to the class not the object instance.
It can modify a class state. Class method creates factory methods

2. Static Method : A static method is a method which is bound to the class not to the object of the class.
A static method can't access or modify class state.
Static method knows nothing about class state, they are utility type methods that takes some parameter and works
upon those parameters. Static methods creates utility functions.


"""
from datetime import date

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def BirthYear(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

