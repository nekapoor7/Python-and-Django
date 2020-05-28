""" Write a Python program to generate all permutations of a list in Python."""
from itertools import permutations
l = list(map(int,input().split()))
per = permutations(l)

for p in per:
    print(p)
