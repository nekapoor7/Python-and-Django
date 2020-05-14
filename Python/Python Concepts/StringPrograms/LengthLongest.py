"""Write a Python function that takes a list of words and returns the length of the longest one."""

words = list(input().split())
le = max(len(c) for c in words)
l = [c for c in words if len(c) == le]
print(l)
long = ''.join(l)
print(long)
print(len(long))