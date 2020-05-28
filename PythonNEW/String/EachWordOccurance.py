"""Write a Python program to count the occurrences of each word in a given sentence."""
from collections import Counter
s = input()
ns = dict(Counter(s.split()))
print(ns)