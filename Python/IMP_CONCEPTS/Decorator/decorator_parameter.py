def evening_greeting(func):
    def function_wrappper(x):
        print("Good evening  " +  func.__name__ + "returns")
        func(x)
    return function_wrappper

    def morning_wrapper(x):
        def function_wrapper(x):
            print("Good Morning " + func.__name__ + "returns")
            func(x)
    return function_wrapper

@evening_greeting
def foo(x):
    print(42)

foo("Hi")
