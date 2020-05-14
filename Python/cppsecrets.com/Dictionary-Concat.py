"""Python Program to Concatenate Two Dictionaries Into One"""

from collections import Counter

A = Counter({'a':1, 'b':2, 'c':3})
B = Counter({'b':3, 'c':4, 'd':5})

res = A+ B

print(res)

def func(*dicts):
    keys = set().union(*dicts)
    return {key:"".join(dic.get(key,'') for dic in dicts)for key in keys}

d = {'a': 'foo', 'b': 'bar', 'c': 'baz'}
d1 = {'a': 'spam', 'c': 'ham', 'x': 'blah'}
print(func(d,d1))