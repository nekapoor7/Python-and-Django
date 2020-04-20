from itertools import chain
from collections import OrderedDict
from operator import getitem

dict ={'Dict1': {'name': 'Ali', 'age': 19},
        'Dict2': {'name': 'Bob', 'age': 21},
        'Dict3': {'name': 'neha', 'age': 10},
        'Dict4': {'name': 'harsh', 'age': 5}}

sum = 0

for key , value in dict.items():
    if value and 'age' in value.keys():
        sum += value['age']

print(sum)

ordered = OrderedDict(sorted(dict.items(),key=lambda i:i[1]['age']))
print(ordered)

'''ordered_key = OrderedDict(sorted(dict.keys(),key=lambda i:i[0]['name']))
print(ordered_key)'''

res = OrderedDict(sorted(dict.items(), key = lambda x: getitem(x[0], 'name')))
print(res)

