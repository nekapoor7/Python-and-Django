"""Write a Python program to find smallest and largest word in a given string."""

s = input().split()
ss = sorted(s,key=str.lower)
print(ss[0])
print(ss[-1])