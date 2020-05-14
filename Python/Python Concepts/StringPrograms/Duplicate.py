"""Write a Python program to remove duplicate characters of a given string."""

from collections import OrderedDict

t = input()
d = ''.join(OrderedDict.fromkeys(t))

print(d)
