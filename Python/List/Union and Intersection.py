"""Python Program to Find the Union of two Lists"""
"""Python Program to Find the Intersection of Two Lists"""

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

set1 = set(list1)
set2 = set(list2)

union = set1.union(set2)
intersection = set1.intersection(set2)

print(union)
print(intersection)