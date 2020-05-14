"""Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)"""

import re

def solution(A):
    if re.search(r'[A-Za-z\d]',A):
        return "OK"
    else:
        return  "Not OK"

A = input()
print(solution(A))