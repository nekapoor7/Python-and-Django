"""Write a Python program to check for a number at the end of a string. """

import re
s =input()
text = re.compile(r'.*[0-9]$')
if text.match(s):
    print(True)
else:
    print(False)
