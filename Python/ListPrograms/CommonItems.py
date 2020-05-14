""" Write a Python program to find common items from two lists."""

list1 = list(input().split())
list2 = list(input().split())
setA = set(map(int,list1))
setB = set(map(int,list2))

common = setA.intersection(setB)
print(common)