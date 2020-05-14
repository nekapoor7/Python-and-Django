"""Python Program to Sum All the Items in a Dictionary"""
dic1 = {'A': 25, 'B': 41, 'C': 32}
print(sum(dic1.values()))

"""Python Program to Multiply All the Items in a Dictionary"""
dic1 = {'A': 25, 'B': 41, 'C': 32}
total = 1

for i in dic1:
    total = total * dic1[i]
print(total)

"""Python Program to Multiply All the Items in a Dictionary"""
dic1 = {'A': 25, 'B': 41, 'C': 32}
dic2 = {'A': 21, 'B': 12, 'C': 62}

dic3 = {key:value * dic2[key] for key,value in dic1.items() if key in dic2}
print(dic3)

"""sum value of two different dictionaries which is having same key"""
from collections import Counter
dic1 = {'A': 25, 'B': 41, 'C': 32}
dic2 = {'A': 21, 'B': 12, 'C': 62}

A = Counter({'A': 25, 'B': 41, 'C': 32})
B = Counter({'A': 21, 'B': 12, 'C': 62})

SumKey = A + B
print(SumKey)


