"""Write a Python program to select the odd items of a list."""
from functools import reduce

list1 = list(input().split())
l = list(map(int,list1))
oddlist = list(filter(lambda varX : varX % 2 != 0,l))

print(oddlist)