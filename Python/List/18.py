"""Write a Python program to generate all permutations of a list in Python."""
from itertools import permutations
n = input()
per = permutations(n)

for p in per:
    print(p)