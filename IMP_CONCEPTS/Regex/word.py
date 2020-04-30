"""Write a Python program that matches a word at the beginning of a string"""

import re

def solution(A):

    if re.search(r'^\w+',A):
        return "OK"
    else:
        return "NOT OK"

A = input()
print(solution(A))