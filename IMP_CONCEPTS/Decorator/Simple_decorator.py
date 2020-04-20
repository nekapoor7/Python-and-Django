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