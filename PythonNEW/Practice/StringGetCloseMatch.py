"""Python | Find all close matches of input string from a list"""
from difflib import get_close_matches
s = list(input().split())
print(get_close_matches(input(),s))