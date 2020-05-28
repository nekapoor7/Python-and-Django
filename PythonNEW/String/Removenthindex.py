"""Write a Python program to remove the nth index character from a nonempty string. """

s = input()
N = int(input())
ns = s[:N] + s[N+1:]
print(ns)