"""Ways to sort list of dictionaries by values in Python – Using itemgetter"""
from operator import itemgetter

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

values = sorted(lis,key=lambda x:x['age'])
print(values)

val = sorted(lis,key=itemgetter('name','age'))
print(val)

"""Ways to sort list of dictionaries by values in Python – Using lambda function"""

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

val1 = sorted(lis,key=lambda x:x['age'])
print(val1)

val2 = sorted(lis,key=lambda x:(x['age'],x['name']))
print(val2)


