"""Write a Python function that takes a list of words and returns the length of the longest one."""

s = input().split()
w = sorted(s,key=len)
print(w[-1])
print(w[0])