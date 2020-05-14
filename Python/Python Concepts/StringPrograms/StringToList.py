"""Write a Python program to convert a string in a list."""

text = input()
l = [x for x in text.split(' ')]
print(l)