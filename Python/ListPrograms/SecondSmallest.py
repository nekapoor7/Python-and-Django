""" Write a Python program to find the second smallest number in a list. """

list1 = list(input().split())
small = min(int(x) for x in list1 if x != min(list1))
print(small)