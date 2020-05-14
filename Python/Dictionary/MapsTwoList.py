"""Write a Python program to map two lists into a dictionary."""

l1 = list(input().split())
l2 = list(input().split())

d = dict(zip(l1,l2))
print(d)