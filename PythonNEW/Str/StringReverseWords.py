"""Write a Python program to reverse words in a string."""

s = input().split()
ss = sorted(s,key=str.lower)
print(ss)