"""Write a Python program to check if a string contains all letters of the alphabet."""
import re

text = input()
s = text.lower()
if re.search('[a-z]+',s):
    print("String contains all letters",len(text))
else:
    print("It contains alphanumeric")