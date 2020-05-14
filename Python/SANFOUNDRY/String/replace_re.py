"""Python Program to Replace all Occurrences of ‘a’ with $ in a String"""

import re

message = input()
replace_string = re.sub('a','$',message)

print(replace_string)


"""Python Program to Take in a String and Replace Every Blank Space with Hyphen"""

blank_hypen = re.sub(' ','-',message)

print(blank_hypen)
