"""Write a Python program to check whether all items of a list is equal to a given string."""

string = input()
list1 = list(input().split())

print(all(c == string for c in list1))

