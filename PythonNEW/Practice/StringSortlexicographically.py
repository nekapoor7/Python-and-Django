"""Write a Python program to sort a string lexicographically."""

s = input()
s1 = sorted(s,key=str.lower)
print(''.join(s1))