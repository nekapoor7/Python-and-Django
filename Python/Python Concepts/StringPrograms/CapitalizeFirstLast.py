"""Write a Python program to capitalize first and last letters of each word of a given string."""

t = input()
s = t[0].capitalize()+t[1:-1]+t[-1].capitalize()
print(s)