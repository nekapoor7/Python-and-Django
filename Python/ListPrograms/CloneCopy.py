"""Write a Python program to clone or copy a list."""

list1 = list(input().split())
list2 = list1[:]

print(list(map(int,list2)))