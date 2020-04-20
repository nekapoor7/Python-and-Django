def greetings(expr):
    def greeting_decorator(func):
        def function_helper(x):
            print(expr + " ," + func.__name__ + "returns")
            func(x)
        return function_helper
    return greeting_decorator

@greetings("καλημερα")
def foo(x):
    print(42)

foo("Hi")