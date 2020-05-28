"""Write a Python program to remove the characters which have odd index values of a given string. """

s = input()
ns = ""
for i in range(len(s)):
    if i % 2 != 0:
        ns = ns + s[i]
print(ns)