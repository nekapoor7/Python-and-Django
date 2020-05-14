"""Write a Python program that matches a string that has an a followed by three 'b'."""

import re

def solution(A):
    if re.findall(r'ab{3,5}?',A):
        return "OK"
    else:
        return "Not OK"

A = input()
print(solution(A))