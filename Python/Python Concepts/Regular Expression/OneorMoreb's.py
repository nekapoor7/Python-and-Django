"""Write a Python program that matches a string that has an a followed by one or more b's. """

import re
s = input()
pat = 'ab+?'
if re.search(pat,s):
    print(True)
else:
    print(False)