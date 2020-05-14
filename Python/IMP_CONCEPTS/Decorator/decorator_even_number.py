def argument_even_number(f):
    def function_wrapper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception ("number is not within range")
    return function_wrapper


@argument_even_number
def even_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(1,10):
    print(i,even_number(i))

#print(even_number(-2))