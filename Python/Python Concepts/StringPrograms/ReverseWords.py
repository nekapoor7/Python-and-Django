"""Write a Python program to reverse words in a string."""

s = str(input())
s1 = ' '.join(s.split()[::-1])
print(s1)