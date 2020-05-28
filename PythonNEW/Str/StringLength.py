"""Write a Python program to calculate the length of a string."""
import re
s = input()
ss = re.findall(r'[a-zA-Z]',s)
print(len(ss))
