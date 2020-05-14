'''Task
You are given a string .
Your task is to find the indices of the start and end of string in .'''

import re

S = input()
k = input()

pattern = re.compile(k)
r = pattern.search(S)
if not r: print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)