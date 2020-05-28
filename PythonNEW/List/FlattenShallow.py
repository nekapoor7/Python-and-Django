""" Write a Python program to flatten a shallow list."""
from itertools import chain
l = [[2,4,3],[1,5,6], [9], [7,9,0]]
ll = list(chain(*l))
print(ll)