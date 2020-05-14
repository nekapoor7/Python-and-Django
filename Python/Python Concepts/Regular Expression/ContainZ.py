"""Write a Python program that matches a word containing 'z'."""
'''
import re
s = input()
pat = '\w*z.\w*'
if re.search(pat,s):
    print("Found match")
else:
    print("No Match")'''


"""Write a Python program that matches a word containing 'z', not at the start or end of the word."""

import re
s = input()
pat = '\Bz\B'
if re.search(pat,s):
    print("Found match")
else:
    print("No Match")