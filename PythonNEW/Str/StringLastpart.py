"""Write a Python program to get the last part of a string before a specified character. Go to the editor
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python"""

import re
s1 = re.sub('\-.*',' ','https://www.w3resource.com/python-exercises')
print(s1)