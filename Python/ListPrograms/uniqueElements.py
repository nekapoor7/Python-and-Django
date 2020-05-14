""" Write a Python program to get unique values from a list."""
from collections import Counter

list1 = list(input().split())
occur = Counter(list1)
list2 = []

d = dict(occur)

for key,value in d.items():
    if value == 1:
        list2.append(key)

print(list2)


