"""What is HashMap and HashTable in Python"""

""" HashTable or HashMap is a data structure that maps keys to its value pairs,its implement the abstract array
data type so this basically make use of function that computes index values that in turn once the element to be searched,
inserted, remove etc.This makes it easier and faster to access data, In general hash table stores key,value pair
and the key is generated using the hash function.

Hash Table or hash Map in python are implemented through built in dictionary data types.
The keys of the dictionary in python are generated via hashing function.The elements of the dicitionary not ordered or 
they can be changed."""

""" Creating Dictionaries
we can create dictionaries in python via 2 ways 
1. Dictionary in python is represented using curly braces. Therefore, to create a dictinary , you can make use of the curly braces.

2. Python provides dict() function that can be used to create dictionaries by passing the key-valye pair
as parameters to it.

Dictionaries are mutable data types and you can update them as in when required."""

my_dict = {'Neha':'7','Harsh':'1','Sam':'2'}
print(my_dict)
print(type(my_dict))

new_dict = dict()
print(new_dict)
print(type(my_dict))

new_dict = dict(Neha='7',Harsh=1)
print(new_dict)
