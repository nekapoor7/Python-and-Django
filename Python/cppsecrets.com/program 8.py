"""Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions"""

import re

text1 = input()
text2 = input()

length1 = re.findall(r'[a-zA-Z]',text1)
length2 = re.findall(r'[a-zA-Z]',text2)

if len(length1) > len(length2):
    print(text1)
else:
    print(text2)
