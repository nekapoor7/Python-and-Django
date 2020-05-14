"""Python Program to Sum All the Items in a Dictionary"""

dict1 = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32','neha':'7','harsh':'25'}

dict1 = dict((key,int(value)) for key,value in dict1.items())

print(sum(dict1.values()))

"""2nd Concepts"""

d = {'key1':1,'key2':14,'key3':47}

print(sum(d.values()))

"""3rd Concept"""

d = {"Labour": [{"load": 5.00},
           {"edge": 0.00},
           {"unload": 5.00},
           {"load": 5.00},
           {"edge": 0.00},
           {"unload": 5.00},
           {"load": 5.00},
           {"edge": 0.00},
           {"unload": 5.00},
           {"load": 0.00},
           {"edge": 0.00},
           {"unload": 0.00},
           {"load": 0.00},
           {"edge": 0.00},
           {"unload": 0.00},
           {"new_val": 5.00},
           {"new_val_2": 5.00}],}

from collections import Counter

dct = Counter()

for ele in d:
    for k,v in d.items():
        dct[k] += v

print(dct)
print(sum(dct.values()))