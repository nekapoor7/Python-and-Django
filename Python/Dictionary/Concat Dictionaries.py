"""Combining two dictionaries into one with the same keys?"""

dic1 = {'A': 25, 'B': 41, 'C': 32}
dic2 = {'A': 21, 'B': 12, 'C': 62}
result = {}
for key in (dic1.keys() | dic2.keys()):
    if key in dic1: result.setdefault(key, []).append(dic1[key])
    if key in dic2: result.setdefault(key, []).append(dic2[key])

print(result)

from collections import Counter
A = {'a':1, 'b':2, 'c':3}
B = {'b':3, 'c':4, 'd':5}

A = Counter({'a':1, 'b':2, 'c':3})
B = Counter({'b':3, 'c':4, 'd':5})

print(A+B)

def func(*dicts):
    keys = set().union(*dicts)
    return {k: "".join(dic.get(k, '') for dic in dicts)for k in keys}

d = {'a': 'foo', 'b':'bar', 'c': 'baz'}
d1 = {'a': 'spam', 'c':'ham', 'x': 'blah'}
print(func(d,d1))




