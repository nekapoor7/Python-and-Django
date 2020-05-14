"""Python Program to Count Number of Lowercase Characters in a String"""

import re

text = input()

lowercount = re.findall(r'[a-z]+',text)   #No Repetition
lowercount1 = re.findall(r'[A-Z]',text)  #Duplicate char

print(len(lowercount))

print(len(lowercount1))