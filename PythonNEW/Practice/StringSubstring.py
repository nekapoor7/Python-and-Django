"""Python | Check if a Substring is Present in a Given String"""

'''s = input()
s1 = input()
if s1 in s:
    print("Substring present")
else:
    print("Substring not present")'''


import re
s1 = input()
s2 = input()

if re.search(s2,s1):
    print("Substring present")
else:
    print("Substring not present")