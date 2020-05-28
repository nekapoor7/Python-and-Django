"""Reverse words in a given String in Python"""

s = input().split()
ss = sorted(s,key=str.lower)
print(' '.join(ss))