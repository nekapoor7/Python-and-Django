""" Write a Python program to find the maximum occurring character in a given string."""

from collections import Counter
text = input()
occur = Counter(text)

print(occur)
d = dict(occur)
m = max(d,key=d.get)
print(m)