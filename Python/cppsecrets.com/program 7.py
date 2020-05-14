"""Python Program to Calculate the Number of Words and the Number of Characters Present in a String"""

import re

text = input()

wordcount = re.findall(r'[a-zA-Z]+',text)
charcount = re.findall(r'[a-zA-Z]',text)

print(len(wordcount))
print(len(charcount))
