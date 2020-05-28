"""Write a Python program to sum all the items in a list."""

l = list(input().split())
sum = sum(map(int,l))
print(sum)