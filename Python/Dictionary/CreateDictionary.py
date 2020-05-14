"""Write a Python program to create a dictionary from two lists without losing duplicate values. Go to the editor
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})"""
from collections import defaultdict

class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
l1 = defaultdict(set)

for c,i in zip(class_list,id_list):
    l1[c].add(i)
print(l1)