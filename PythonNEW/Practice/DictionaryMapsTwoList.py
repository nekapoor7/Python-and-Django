"""Write a Python program to map two lists into a dictionary."""

l = list(input().split())
l1 = list(input().split())
d = dict(zip(l,l1))
print(d)