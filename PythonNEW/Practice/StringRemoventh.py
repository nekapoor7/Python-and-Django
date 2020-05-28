""" Write a Python program to remove the nth index character from a nonempty string."""

s = input()
n = int(input())
ss = s[:n] + s[n+1:]
print(ss)