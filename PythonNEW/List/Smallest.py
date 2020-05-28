"""Write a Python program to get the smallest number from a list."""

l = list(input().split())
m = min(int(x) for x in l if x == min(l))
print(m)