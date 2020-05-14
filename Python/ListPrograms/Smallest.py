"""Write a Python program to get the smallest number from a list."""

list1 = list(input().split())
print(list1)
small = min(int(x) for x in list1 if x == min(list1))
print(small)

