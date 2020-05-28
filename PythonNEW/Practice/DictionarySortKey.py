"""Write a Python script to sort (ascending and descending) a dictionary by key. """
from operator import itemgetter

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
dd = sorted(d.items(),key=itemgetter(0))
print(dd)

d1 = sorted(d.items(),key=lambda x:x[0])
print(d1)