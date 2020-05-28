""" Write a Python program to print the numbers of a specified list after removing even numbers from it."""

l = list(input().split())
l1 = []

for i in map(int,l):
    if i % 2 != 0:
        l1.append(i)
print(l1)