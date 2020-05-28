"""Write a Python program to change a given string to a new string where the first and last chars have been exchanged"""

s = input()
ns = s[-1:] + s[1:-1] + s[0]
print(ns)