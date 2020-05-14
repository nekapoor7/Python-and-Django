"""Python Program to Accept Three Digits and Print all Possible Combinations from the Digits"""
from itertools import permutations

num = int(input())

value = map(int,str(num))

permutation = permutations(value)

for p in permutation:
    print(p)

