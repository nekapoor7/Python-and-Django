"""Write a Python program to find sequences of lowercase letters joined with a underscore. """

import re
s = input()
pat = '[a-z]+_[a-z]+$'
if re.search(pat,s):
    print("Found a Match")
else:
    print("Match Not Found")