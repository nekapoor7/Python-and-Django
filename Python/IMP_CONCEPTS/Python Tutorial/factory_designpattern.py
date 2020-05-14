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
b= get('b')
b.print()