"""Write a Python program to get the largest number from a list."""
"""Write a Python program to find the second largest number in a list."""

l = list(input().split())
m = max(int(x) for x in l if x == max(l))
m1 = max(int(x) for x in l if x != max(l))
print(m)
print(m1)



