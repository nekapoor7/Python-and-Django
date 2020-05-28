"""Write a Python program to find the second largest number in a list."""

l = list(input().split())
m = max(int(x) for x in l if x !=max(l))
print(m)