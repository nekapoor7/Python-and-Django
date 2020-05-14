"""Write a Python program to find the sequences of one upper case letter followed by lower case letters. """

import re
s = input()
pat = '[A-Z]+[a-z]+$'
if re.search(pat,s):
    print("Found Match")
else:
    print("Match Not Found")