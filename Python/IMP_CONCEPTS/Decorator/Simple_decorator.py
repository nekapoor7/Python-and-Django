""" What is Decorator?

-> Very powerful and useful tool in Python since it allows programmers to modify the behavior of function and classes.
-> Allows us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
-> In Decorators, functions are taken as the arguments into another function and then called inside the wrapper function.

"""

def our_decorator(func):
    def function_wrapper(x):
        print("Before Calling " + func.__name__)
        func(x)
        print("After Calling   "  + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Function is called through foo" +  str(x))


foo("Hi")