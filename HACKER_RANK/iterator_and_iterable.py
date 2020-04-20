'''The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of
lowercase English letters. For a given integer , you can select any indices (assume

-based indexing) with a uniform probability from the list.

Find the probability that at least one of the
indices selected will contain the letter: ''. '''

from itertools import combinations

N = int(input())
S = input().split(' ')
K = int(input())

num = 0
den = 0

for c in combinations(S, K):
    den += 1
    num += 'a' in c

print(float(num) / den)