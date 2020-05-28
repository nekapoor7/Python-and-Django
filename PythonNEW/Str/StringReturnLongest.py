"""Write a Python function that takes a list of words and returns the length of the longest one."""

s = str(input())
ss = sorted(s.split(),key=len)
print(ss[-1])