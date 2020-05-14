#Program to find all the permutations of a string

import itertools

string = str(input())
string = list(string)
count = 0

permutations = itertools.permutations(string)

for p in permutations:
    print(p)
    count += 1

print(count)