"""Write a Python program to multiplies all the items in a list."""
from functools import reduce

l = list(input().split())
l = map(int,l)
m = reduce(lambda x,y : x * y,l)
print(m)