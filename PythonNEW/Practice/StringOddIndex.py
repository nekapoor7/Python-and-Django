"""Write a Python program to remove the characters which have odd index values of a given string. """

s = input()
res = ""

for i in range(len(s)):
    if i % 2 != 0:
        res = res + s[i]
print(res)