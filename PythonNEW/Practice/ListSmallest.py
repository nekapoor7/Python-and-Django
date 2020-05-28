"""Write a Python program to get the smallest number from a list."""
"""Write a Python program to find the second smallest number in a list."""

l = list(input().split())
m = min(int(x) for x in l if x == min(l))
m1 = min(int(x) for x in l if x!= min(l))
print(m)
print(m1)