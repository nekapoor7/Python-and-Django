"""Write a Python program to check a list is empty or not."""

list1 = list(input().split())

if len(list1) < 1:
    print("List is empty")
else:
    print("List has elements")