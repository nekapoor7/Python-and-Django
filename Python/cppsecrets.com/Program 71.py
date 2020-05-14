"""Python Program to find the factorial of a number without recursion"""

def factorial_number(f):
    def helper(x):
        if x > 0 and type(x) == int:
            return f(x)
        else:
            raise Exception("Entered number is negative")
    return helper

@factorial_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

num = int(input())
print(factorial(num))
