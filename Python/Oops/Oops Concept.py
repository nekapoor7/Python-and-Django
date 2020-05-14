"""What Is Object-Oriented Programming (OOP)?"""

"""OOP is a programming paradigm which provides a means of structuring  programs so that properties and behaviors 
are bundled into individual objects."""

'''Class in Python '''

'''Classes are used to create a new user-defined data structures that contain arbitrary information
   Class just provides structure '''

'''Python Object'''

'''An instance is a copy of class with actual values, an object belonging to a specific class
'''
''' How to Define Class'''

'''class Dog:
        pass'''

'''# Python 2.x Class Definition:
class Dog(object):
    pass
    
In Python3 there is no longer necessary because it is the implicit default.     
'''

"""Instance Attribute 

All classes create objects, and all objects contain characteristics called attributes. Use the __init__() 
method to initialize an object's initial attributes by giving them their default value (or state).This method
must have at least one argument as well as the self variable, which refers to the object itself.

class Dog:
    #instance attributes
    def __init__(self,name,age):
        self.name
        self.age
        
In the case of our Dog() class,each dog has a specific name and age, which is obviously important to know for when 
you start actually creating different dogs.

Similarly, the self variable is also an instance of class. Since instance of a class have varying values
we could state Dog.name = name rather than self.name = name. But since not all dogs share same name, we need to be able 
to assign different values to different instances         


"""
