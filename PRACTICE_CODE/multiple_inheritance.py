#Python support Multiple Inheritance?

class Base1(object):
    def __init__(self):
        self.str1 = "Geeks1"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Geeks2"
        print("Base2")

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStr(self):
        print(self.str1,self.str2)

ob = Derived()
ob.printStr()




