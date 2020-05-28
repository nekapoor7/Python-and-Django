"""Write a Python program to access a function inside a function."""

def factorial_number(f):
    def inner(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Number is a negative")
    return inner

@factorial_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())
print(factorial(n))