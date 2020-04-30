"""Write a Python program that matches a word at the end of string, with optional punctuation."""

import re

def solution(A):
    if re.search(r'\w?$'):
        return