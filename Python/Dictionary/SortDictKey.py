""" Write a Python program to sort a dictionary by key."""

from collections import OrderedDict

d = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

#dd = {key:value for key,value in d.items()}
k = OrderedDict(sorted(d.items()))
k1 = dict(k)

print(k1)

