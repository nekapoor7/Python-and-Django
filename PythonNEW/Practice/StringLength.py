"""Find length of a string in python (4 ways)"""
import re
s = input()
s1 = s.lower()
ss = re.findall(r'[a-z]',s1)
print(len(ss))