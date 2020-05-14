"""Write a Python program to check whether a string starts with specified characters. """

s = input()
ch = input()
if s.startswith(ch):
    print("start with specfied char")
else:
    print(s)

"""Special Characters"""
'''
import re

s = input()
if re.findall(r'^[!@#$%^&*()_+\-=\[\]{};"\\|,.<>\/?]',s):
    print("Start with special characters")
else:
    print(s)'''