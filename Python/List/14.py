"""Write a Python program to print the numbers of a specified list after removing even numbers from it."""
l = [3,5,2,11,6,8]
od = list(filter(lambda x : x % 2 != 0,l))
print(od)

""" Write a Python program to shuffle and print a specified list."""

from random import shuffle
shuffle(l)
print(l)
