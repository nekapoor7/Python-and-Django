from datetime import date

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def BirthYear(cls,name,year):
        return cls(name,date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('Neha Kapoor',30)
person2 = Person.BirthYear('Neha Kapoor',1989)

print(person1.age)
print(person2.age)

print(Person.isAdult(30))