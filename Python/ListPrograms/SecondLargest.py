"""Write a Python program to find the second largest number in a list."""

list1 = list(input().split())
large = max(int(x) for x in list1 if x != max(list1))
print(large)