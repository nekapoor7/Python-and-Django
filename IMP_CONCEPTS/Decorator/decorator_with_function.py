def our_decorator(func):
    def function_wrapper(x):
        print("Before Calling" + func.__name__)
        res = func(x)
        print(res)
        print("After Calling" + func.__name__)
    return function_wrapper

@our_decorator
def succ(n):
    return n + 1


succ(10)