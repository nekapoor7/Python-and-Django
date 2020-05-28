""" Write a Python program to get the frequency of the elements in a list."""
from collections import Counter
l = list(input().split())
c = Counter(l)
print(c)