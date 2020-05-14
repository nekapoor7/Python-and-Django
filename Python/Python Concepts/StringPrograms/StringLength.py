"""Write a Python program to calculate the length of a string."""

import re
text = input()
l = re.findall(r'[a-zA-Z]',text)
print(len(l))