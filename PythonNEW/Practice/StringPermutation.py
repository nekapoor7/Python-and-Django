"""Python | Permutation of a given string using inbuilt function"""
from itertools import permutations

s = input()
per = permutations(s)
for p in per:
    print(p)