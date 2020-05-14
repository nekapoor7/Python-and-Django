"""Python Program to Find Element Occurring Odd Number of Times in a List"""

from collections import Counter
list1 = list(map(int,input().split()))
list2 = []

occur = Counter(list1)

dict1 = dict(occur)
print(type(dict1))
print(dict1)

for key,value in dict1.items():
    if value % 2 != 0:
        list2.append(key)

print(list2)


