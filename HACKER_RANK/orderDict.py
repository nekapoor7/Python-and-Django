'''collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry, the original insertion position is left unchanged. '''

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)