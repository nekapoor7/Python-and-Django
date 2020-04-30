"""Write a Python program that matches a string that has an a followed by zero or one 'b'"""

import re

def solution(A):
    if re.search(r'ab+',A):
        return "OK"
    else:
        return "Not Ok"

A = input()
print(solution(A))

