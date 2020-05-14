lst = [
{'Name': 'A', 'amt':100},
{'Name': 'B', 'amt':200},
{'Name': 'A', 'amt':300},
{'Name': 'C', 'amt':400},
{'Name': 'C', 'amt':500},
{'Name': 'A', 'amt':600}]

import itertools as it
keyfunc = lambda x: x['Name']

groups = it.groupby(sorted(lst, key=keyfunc), keyfunc)
dict1 = [{'Name':k, 'amt':sum(x['amt'] for x in g)} for k, g in groups]

print(dict1)
