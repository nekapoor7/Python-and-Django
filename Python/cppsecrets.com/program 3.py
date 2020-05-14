"""Python Program to Count the Number of Vowels in a String"""

import re

text = input()

vcount = re.findall(r'[aeiouAEIOU]+',text)
print(len(vcount))