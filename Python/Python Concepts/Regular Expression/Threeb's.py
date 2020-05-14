"""Write a Python program that matches a string that has an a followed by three 'b'."""

import re
s = input()

pat = 'ab{3}?'
if re.search(pat,s):
    print(True)
else:
    print(False)

