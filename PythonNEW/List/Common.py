""" Write a Python program to find common items from two lists."""

l = list(input().split())
l1 = list(input().split())

common = set(l).intersection(set(l1))
print(list(common))