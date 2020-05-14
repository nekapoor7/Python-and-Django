""" Write a Python program to generate all permutations of a list in Python."""
from itertools import permutations

list1 = list(input().split())
per = permutations(list1)

for p in per:
    print(p)