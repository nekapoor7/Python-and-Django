"""Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
 Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""

import re
t = input()
upper = re.findall(r'[A-Z]',t)
lower = re.findall(r'[a-z]',t)
print(len(upper))
print(len(lower))