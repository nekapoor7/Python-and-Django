"""Python program to print fibonacci series"""

def factorial_number(f):
    def inner(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Entered number is Negative")
    return inner

@factorial_number
def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

n = int(input())
print(factorial(n))