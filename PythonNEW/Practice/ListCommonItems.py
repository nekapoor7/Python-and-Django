""" Write a Python program to find common items from two lists. """

l = list(input().split())
ll = list(input().split())

common = list(set(l).intersection(set(ll)))
print(' '.join(common))