"""Write a Python program to compute sum of digits of a given string."""

import re
s = input()
ss = re.findall(r'[0-9]',s)
print(sum(map(int,ss)))
