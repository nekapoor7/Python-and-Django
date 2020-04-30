"""Operator Overloading

If an operator performs additional actions other than what it is meant for , it is called operator overloading.

"""

class A:

    def __init__(self,a):
        self.a = a

    #adding two objects
    def __add__(self, other):
        return self.a + other.a

ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
