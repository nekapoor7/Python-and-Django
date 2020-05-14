"""Write a Python script to sort (ascending and descending) a dictionary by key."""

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

from collections import OrderedDict
from collections import Counter
from operator import itemgetter

k = Counter(sorted(d.keys()))
k1 = Counter(sorted(d.keys(),reverse=True))
d1 = {k:int(v) for k,v in d.items()}
v = OrderedDict(sorted(d1.items(),key=itemgetter(1)))
v1 = OrderedDict(sorted(d1.items(),key=itemgetter(1),reverse=True))

print(k)
print(k1)
print(dict(v))
print(dict(v1))

"""Write a Python script to sort (ascending and descending) a dictionary by value."""



