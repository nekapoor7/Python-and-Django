"""Python Program to Calculate the Number of Digits and Letters in a String"""

import re
text = input()

lettercount = re.findall(r'[a-zA-Z]',text)
digcount = re.findall(r'\d',text)

print(len(lettercount))
print(len(digcount))
