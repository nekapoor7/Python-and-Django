""" Write a Python program to get the frequency of the elements in a list."""

from collections import Counter
list1 = list(input().split())
occur = Counter(list1)

print(occur)