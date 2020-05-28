"""Python | Program to accept the strings which contains all vowels"""
import re
s = input()
s1 = s.lower()
ss = re.findall(r'[aeiou]',s1)
print(len(ss))
print(ss)