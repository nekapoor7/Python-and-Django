"""Write a Python program to get the largest number from a list. """

l = list(input().split())
m = max(int(x) for x in l if x == max(l))
print(m)