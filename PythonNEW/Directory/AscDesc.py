"""Write a Python script to sort (ascending and descending) a dictionary by value."""
from collections import Counter
from operator import itemgetter
from collections import OrderedDict
d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
k = OrderedDict(sorted(d.items()))
k1 = OrderedDict(sorted(d.items(),reverse=True))
print(k)
print(k1)

d1 = {key:int(value) for key,value in d.items()}
v = OrderedDict(sorted(d.items(),key=itemgetter(1)))
v1 = OrderedDict(sorted(d.items(),key=itemgetter(1),reverse=True))
print(v)
print(v1)