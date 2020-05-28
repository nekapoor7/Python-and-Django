"""Write a Python program to multiplies all the items in a list."""
from functools import reduce

l = list(input().split())
l1 = map(int,l)
m = reduce(lambda x , y: x * y,l1)
print(m)