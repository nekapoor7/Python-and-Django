""" Design Pattern

-> provides a general solutions for the common problem.
-> shows relationship between classes and objects.
-> represents an idea
-> Makes code reusable, maintainable and flexible.

3 types of Design Pattern
1. Creational -> Factory Method, Singleton (About class instantiation and objects Creations)
2.Structural -> Facade, Decorator (Organizing different classes and objects to form larger structures and
provide new functionality.
3. Behavioral  -> Iterator (Identifying common communication patterns between objects and realize these patterns).

1. Singleton: used to create one and only one instance of a class and provide global point of access to it,
so that it can be accessible by several clients
Example: File Manager
The class itself takes the responsibilty of creation of not more than one instance and can provide well defined
access point for multiple applications.

"""

class Metaclass(type):

    """ This is the Singleton Design Pattern"""

    __instance = {}

    def __call__(cls, *args, **kwargs):

        """ If an istance is created don't create the new instance"""

        if cls not in cls.__instance:
            cls.__instance[cls] = super(Metaclass,cls).__call__(*args, **kwargs)
            return cls.__instance[cls]

class A(metaclass=Metaclass):

    def __init__(self):
        pass

obj = A()
print(obj)
obj1 = A()
print(obj1)

"""Factory Method uses subclasses to create an object of derived class of another class.
Create an object through subclass. 
Redefine a method in derived class which will decide which subclass 
to instantiate."""

"""Factory Design Pattern"""

class A(object):

    def __init__(self):
        pass

    def methodA(self):
        print("Hello I am Method A")

    def print(self):
        print("A")

class B(object):

    def __init__(self):
        pass

    def methodB(self):
        print("Hello I am Method B")

    def print(self):
        print("B")

def get(obj=''):
    object = dict(a=A(),b=B())
    return object[obj]

a = get('a')
a.print()
b = get('b')
b.print()

"""Abstract Factory Method 

Provides an interface for creating families of related or dependent objects 
without specifying their concrete classes.

"""
"""
Facade design pattern 

Facade design pattern hides the complexities of the system and provides an interface to the client using 
which the client can access the system.This type of design pattern comes under structural design pattern
as this pattern adds an interface to an existing system to hide its complexities.

This pattern involves a single class which provides simplified methods required by client and delegates 
calls to method of existing system classes.

"""


class Sensor(object):
    def __init__(self):
        pass

    def sensorON(self):
        print("Sensor is ON")

    def sensorOFF(self):
        print("Sensor is OFF")


class Smoke(object):
    def __init__(self):
        pass

    def smokeON(self):
        print("Smoke is ON")

    def smokeOFF(self):
        print("Smoke is OFF")


class Lights(object):
    def __init__(self):
        pass

    def lightsON(self):
        print("Light is ON")

    def lightsOFF(self):
        print("Light is OFF")


class Facade(object):

    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Lights()

    def emergency(self):
        self._sensor.sensorON()
        self._light.lightsON()
        self._smoke.smokeON()

    def NotEmergency(self):
        self._sensor.sensorOFF()
        self._light.lightsOFF()
        self._smoke.smokeOFF()


if __name__ == "__main__":
    facade = Facade()
    sensor = int(input())

    if sensor > 60:
        facade.emergency()
    else:
        facade.NotEmergency()
