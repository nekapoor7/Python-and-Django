""" Write a Python program to print the numbers of a specified list after removing even numbers from it."""

l = list(input().split())
l = map(int,l)
ll = list(filter(lambda x: x %2 != 0,l))
print(ll)


