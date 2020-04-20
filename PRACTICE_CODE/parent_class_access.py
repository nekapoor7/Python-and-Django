#How to access parent members in a subclass?

class Base(object):
    def __init__(self,x):
        self.x = x

class Derived(Base):

    # Constructor
    def __init__(self,x,y):
        Base.x = x
        self.y = y

    def printXY(self):
        # print(self.x, self.y) will also work
        print(Base.x,self.y)


d = Derived(10,20)
d.printXY()