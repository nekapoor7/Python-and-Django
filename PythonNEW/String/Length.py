"""Write a Python program to calculate the length of a string."""

import re
s = input()
l = re.findall(r'[a-zA-Z]',s)
print(len(l))