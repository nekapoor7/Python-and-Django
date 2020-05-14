def factorial_number(s):
    def helper(x):
            if x > 0  and type(x) == int:
                return s(x)
            else:
                raise Exception("Argument is not an Integer and Negative")
    return helper

@factorial_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int (input())
#for i in range(1,10):
print(factorial(num))

