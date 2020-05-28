"""Write a Python program to remove a newline in Python."""
import re
line = 'neha\n'
l=line.strip()
l=re.sub("\n","",l)

print(l)
