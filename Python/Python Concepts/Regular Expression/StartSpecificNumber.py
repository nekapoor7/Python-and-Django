"""Write a Python program where a string will start with a specific number. """

'''import re
s = input()
pat = re.compile(r'^5')
if pat.match(s):
    print(True)
else:
    print(False)'''


"""Write a Python program that matches a word at the beginning of a string."""

import re
s = input()
pat = re.compile(r'^\w+')
if pat.match(s):
    print(True)
else:
    print(False)