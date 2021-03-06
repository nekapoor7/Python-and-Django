import math

def CheckPerfect(x):
    i = int(math.sqrt(x))
    return x == i*i

def CheckFibo(n):
    if CheckPerfect(5*n*n + 4) or CheckPerfect(5*n*n - 4):
        print("Fibonacci")
    else:
        print("Not Fibonacci")

num = int(input())
CheckFibo(num)