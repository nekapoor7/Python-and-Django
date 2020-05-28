"""Python program to count number of vowels using sets in given string"""
import re
s = input()
s1 = s.lower()
ss = re.findall(r'[aeiou]',s1)
print(set(ss))