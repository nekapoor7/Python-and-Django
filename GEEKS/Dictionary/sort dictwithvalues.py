"""Ways to sort list of dictionaries by values in Python – Using lambda function"""
from operator import itemgetter

lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 30 },
{ "name" : "Nikhil" , "age" : 19 },
{ "name" : "Neha" , "age" : 30 },
{ "name" : "Harsh" , "age" : 33 }]


sorted_age = sorted(lis, key=lambda x: x['age'])

sorted_name = sorted(lis, key=lambda x: (x['age'], x['name']))

descending_sort = sorted(lis, key=lambda x: x['age'], reverse=True)

print(sorted_age)
print(sorted_name)
print(descending_sort)

"""Ways to sort list of dictionaries by values in Python – Using itemgetter"""

age_sort = sorted(lis, key=itemgetter('age'))

age_name_sort = sorted(lis, key=itemgetter('name','age'))

print(age_name_sort)
print(age_sort)