"""Write a Python program that matches a string that has an a followed by two to three 'b'. """

import re

def solution(A):

    if re.match(r'ab{2,3}?',A):
        return "OK"
    else:
        return "Not OK"

A = input()
print(solution(A))