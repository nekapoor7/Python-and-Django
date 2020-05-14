"""Decorator"""

"""
Functional Decorator : A functional decorator is a function that takes a function as its only parameter
 and return a function. It means to wrap a functionality with the same code over again an again.
 
 We use @func_name to specify a decorator to be applied on another function. 
 
 Decorators are powerful tool in Python since it allows programmers to modify the behavior 
 of a function or class. Decorators are allows us to wrap another function in order to extend 
 the behavior of wrapped function without permanently modifying it.
 
Recursion is a programming technique where a function itself repeatedly till a termination condition is met.
Some of the examples are fibonacci and factorial. But the issue with recursion, there can be chances that the sub 
problem that is already solved is being solved again, it leads to an overhead.

Memorization is a technique of recording the intermediate result so that it can be used to avoid repeated 
calculations and speed up the program. In Python, Memorization can be done with the help of functional decorators.

1. A function called memoize_factorial has been defined. 
It’s main purpose is to store the intermediate results in the variable called memory.
2. The second function called facto is the function to calculate the factorial. 
It has been annotated by a decorator(the function memoize_factorial). 
The facto has access to the memory variable as a result of the concept of closures.The annotation is equivalent to writing,

facto = memoize_factorial(facto)

3. When facto(5) is called, the recursive operations take place in addition to the storage of intermediate results. 
Every time a calculation needs to be done, it is checked if the result is available in memory. 
If yes, then it is used, else, the value is calculated and is stored in memory.
"""
# Memorization in Python :

def memorize_factorial(f):
    memory =  {}

    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]
    return inner

@memorize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)

n = int(input())
print(facto(n))

#Decorators with parameters in Python

def decorator(*args,**kwargs):
    print("Inside Decorator")

    def inner(func):
        print("inside inner function")
        print("I like",kwargs['like'])

        func()
    return inner

@decorator(like='neha kapoor')
def myfunc():
    print("Good Bye Take Care!")

"""Property Decorator"""

class Test:

    myvar = 22222

    def __init__(self,num=1):
        self.num = num
        self.__num = 122

    def get_value(self):
        return self.__num

    def set_value(self,num):
        self.__num = num

    @property
    def methodA(self):
        print("Hi I am Method A")

    @staticmethod
    def methodB():
        print("I am method B")

    def __str__(self):
        return "Object Test"

    def classvaraccess(cls):
        print("Class variable access {} ".format(cls.myvar))

if __name__ == "__main__":
    obj = Test()
    print(obj)
    print(obj.methodA)
    print(obj.methodB())
    print(obj.classvaraccess())

