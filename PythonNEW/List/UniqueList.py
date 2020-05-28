""" Write a Python program to get unique values from a list."""

l = list(input().split())
l = map(int,l)
s = set(l)
print(list(s))