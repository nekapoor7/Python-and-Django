"""Write a Python program to count and display the vowels of a given text. """

import re

text = input()
v = re.findall(r'[aeiouAEIOU]',text)
setA = set(v)
print(len(setA))

