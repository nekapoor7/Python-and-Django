"""Python Program to Calculate the Length of a String Without Using a Library Function"""

import re
text = input()

strlength = re.findall(r'[A-Za-z]+',text)

print(len(strlength))