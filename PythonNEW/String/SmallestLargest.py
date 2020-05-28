"""Write a Python program to find smallest and largest word in a given string."""

s = input()
l = s.split()
m = min(l,key=len)
n = max(l,key=len)
print(m)
print(n)