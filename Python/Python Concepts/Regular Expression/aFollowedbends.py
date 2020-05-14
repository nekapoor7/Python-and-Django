"""Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. """

import re
s = input()
pat = r'a.*?b$'
if re.search(pat,s):
    print("Found Match")
else:
    print("Match Not Found")