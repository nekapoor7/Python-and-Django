""" Write a Python program to shuffle and print a specified list. """
from random import shuffle

l = list(input().split())
shuffle(l)
print(l)
