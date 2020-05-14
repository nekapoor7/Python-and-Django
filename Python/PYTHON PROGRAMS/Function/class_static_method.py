from datetime import date

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return(cls(name,date.today().year - year))

    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('Neha',30)
person2 = Person.fromBirthYear('Neha',1989)

print(person1.age)
print(person2.age)

static_args = Person.isAdult(30)
print(static_args)