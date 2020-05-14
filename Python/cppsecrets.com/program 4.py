"""Python Program to Take in a String and Replace Every Blank Space with Hyphen"""

import re

text = input()

new_string = re.sub(' ','-',text)
print(new_string)