"""Extracting email addresses using regular expressions in Python"""

import re

def solution(A):
    email = re.findall(r'\S+@\S+',A)
    res = " ".join(email)
    return res

A = input()
print(solution(A))