""" Write a Python program to count and display the vowels of a given text."""

import re
s = input()
s1 = s.lower()
vcount = re.findall(r'[aeiou]',s1)
print(vcount)
print(len(vcount))