"""Write a Python program to shuffle and print a specified list. """

from random import shuffle

words = list(input().split())
shuffle(words)
print(words)