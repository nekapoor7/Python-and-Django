"""Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String"""

import re

text = input()

lowercount = re.findall(r'[a-z]',text)
uppercount = re.findall(r'[A-Z]',text)

print(len(lowercount))
print(len(uppercount))