""" Write a Python program to find the first repeated character in a given string."""
from collections import Counter
s = input()
c = Counter(s)
for k in c:
    if c[k] > 1:
        print(k)
        break