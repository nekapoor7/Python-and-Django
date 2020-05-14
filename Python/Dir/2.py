"""Write a Python script to merge two Python dictionaries."""
from functools import reduce

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d2.update(d1)
print(d2)

"""Write a Python program to iterate over dictionaries using for loops."""
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for key, value in d.items():
    print(key,'corresponds to',value)

"""Write a Python program to sum all the items in a dictionary."""
d1 = {'a': 100, 'b': 200, 'c':300}
dd = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
print(sum(map(int,dd.values())))

""" Write a Python program to multiply all the items in a dictionary. """
total = 1
for key in d1:
    total = total * d1[key]
print(total)

"""Write a Python program to remove a key from a dictionary."""
k = [str(x) for x in input().split()]
kk = {key:int(value) for key,value in dd.items() if key not in k}
print(kk)

"""Write a Python program to map two lists into a dictionary."""
l = ['Red', 'Green', 'White']
l1 = ['Green', 'White', 'Black']
res = dict(zip(l,l1))
print(res)

"""Write a Python program to sort a dictionary by key."""
from collections import OrderedDict
dd = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}
kk = OrderedDict(sorted(dd.items()))
kk1 = OrderedDict(sorted(dd.items(),reverse=True))
print(kk)
print(kk1)

"""Write a Python program to get the maximum and minimum value in a dictionary."""
print(max(map(int,dd.values())))
print(min(map(int,dd.values())))

