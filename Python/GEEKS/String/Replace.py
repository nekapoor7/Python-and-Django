"""Python Program to Replace all Occurrences of ‘a’ with $ in a String"""

import re

string1 = input()

str_occurance = re.sub(r'a','$',string1)

print(str_occurance)

"""Python Program to Take in a String and Replace Every Blank Space with Hyphen"""

string2 = input()

replce_hypen = re.sub(' ','-',string2)
print(replce_hypen)