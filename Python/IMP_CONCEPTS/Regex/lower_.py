"""Write a Python program to find sequences of lowercase letters joined with a underscore"""

import re

def solution(A):
    if re.findall(r'^[a-z]+_[a-z]+$',A):
        return "OK"
    else:
        return "Not OK"

A = input()
print(solution(A))
