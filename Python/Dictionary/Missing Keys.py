"""Handling missing keys in Python dictionaries"""

from collections import defaultdict

keys = input()

#dict2 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dict2 = defaultdict(lambda :'Key not found')

dict2['neha'] = 7
dict2['harsh'] = 25

print(dict2[keys])

L = [{0: 1, 1: 7, 2: 3, 4: 8}, {0: 3, 2: 6}, {1: 2, 4: 6}, {0: 2, 3: 2}]

allkeys = frozenset().union(*L)
for i in L:
    for j in allkeys:
        if j not in i:
            i[j]=0

print(L)