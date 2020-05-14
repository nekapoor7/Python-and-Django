"""Python Program to Replace all Occurrences of a with a $ in a String"""

import re

text = input()

newstr = re.sub('a','$',text)

print(newstr)