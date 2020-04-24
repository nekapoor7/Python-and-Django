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