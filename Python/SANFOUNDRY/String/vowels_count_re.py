""" Count number of vowels"""

import re
message = input()
message = message.lower()
string = input()
print(len(re.findall(r'[aeiou]',message)))

"""" Consonant in a string"""

con_count = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]',message))
print(con_count)

""" Count Lowercase in a string"""

lower_count = len(re.findall(r'[a-z]',string))
print(lower_count)

""" Count Uppercase in a String"""

upper_count = len(re.findall(r'[A-Z]',string))
print(upper_count)

