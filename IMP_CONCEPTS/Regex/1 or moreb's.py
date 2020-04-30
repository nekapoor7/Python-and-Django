"""Write a Python program that matches a string that has an a followed by one or more b's."""

import re

def solution(A):
    if re.match(r'ab{1}\w*',A):
        return "OK"
    else:
        return "Not OK"

A = input()
print(solution(A))