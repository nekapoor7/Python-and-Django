#1st Method

class A(object):
    def __init__(self):
        pass

#2nd Method

class B(object):
    def __call__(cls, *args, **kwargs):
        return super(B,cls).__call__(cls)

#3rd Method

class C(object):
    def __new__(cls, *args, **kwargs):
        print("Creating an object")
        return super(C,cls).__new__(cls,*args,**kwargs)

    def __init__(self,*args,**kwargs):
        print("Creating an instance of class")
        super(C,self).__init__(*args,**kwargs)


A1 = A()
print(A1)
B1 = B()
print(B1)
C1 = C()
print(C1)