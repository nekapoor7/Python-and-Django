"""Write a Python program that matches a string that has an a followed by zero or one 'b'."""

import re
s = input()
pat = 'ab?'

if re.search(pat,s):
    print(True)
else:
    print(False)