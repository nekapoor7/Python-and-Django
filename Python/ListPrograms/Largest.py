"""Write a Python program to get the largest number from a list."""

list1 = list(input().split())
print(list1)
largest = max(int(x) for x in list1 if x == max(list1))
print(largest)
