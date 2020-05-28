"""Write a Python program to change a given string to a new string where the first and last chars have been exchanged. """

s = input()
ns = s[-2:] + s[:2]
print(ns)