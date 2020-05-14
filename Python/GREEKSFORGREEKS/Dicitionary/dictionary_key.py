from collections import OrderedDict

my_dict={}

limit = int(input())

for i in range(limit):
    key = input()
    value = input()
    my_dict.update({key:value})
print(my_dict)

dict1 = OrderedDict(sorted(my_dict.items()))
print(dict1)