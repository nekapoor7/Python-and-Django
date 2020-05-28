"""Write a Python program to lowercase first n characters in a string."""

s = input()
N = int(input())

ns = s[:N+1].lower() + s[N:]
print(ns)