"""Write a Python script to sort (ascending and descending) a dictionary by value."""
from collections import OrderedDict
from operator import itemgetter

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dd = {key:int(value) for key,value in d.items()}
d1 = OrderedDict(sorted(dd.items(),key=itemgetter(1),reverse=True))
print(d1)

