"""Python Program to Find the Factorial of a Number Using Recursion"""

def factorial_number(s):
    def helper(x):
        if x > 0 and type(x) == int:
            return s(x)
        else:
            raise Exception("Number is negative")
    return helper

@factorial_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))