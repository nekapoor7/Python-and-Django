"""Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores."""

import re
s = input()
pat = '^\w*$'
if re.search(pat,s):
    print("Match Found")
else:
    print("Match Not Found")
