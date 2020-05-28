"""Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})"""
from collections import defaultdict
l = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
l1 = [1, 2, 2, 3]
d = defaultdict(set)
for c, i in zip(l,l1):
    d[c].add(i)
print(d)