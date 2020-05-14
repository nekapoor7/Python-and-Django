"""Write a Python program to lowercase first n characters in a string."""

text = input()
n = int(input())

newstring = text[:n].lower() + text[n:]

print(newstring)