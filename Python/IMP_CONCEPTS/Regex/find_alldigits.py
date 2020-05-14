"""Find all the numbers in a string using regular expression in Python"""

import re

def solution(A):
    number = re.findall(r'[0-9]+',A)
    res = " ".join(number)
    return res

A = input()
print(solution(A))