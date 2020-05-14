"""Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)."""

import re
def specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(specific_char(input()))
print(specific_char(input()))


