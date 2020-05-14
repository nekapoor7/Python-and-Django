"""Python Program to find LCM"""

from functools import reduce
import math

a , b = list(map(int,input().split()))

lcm = (a * b/math.gcd(a,b))

print(lcm)

'''from functools import reduce
from fractions import gcd

def lcm(a, b):
    return a * b / gcd(a, b)

def lcms(*numbers):
     return reduce(lcm, numbers)

def gcds(*numbers):
     return reduce(gcd, numbers)'''