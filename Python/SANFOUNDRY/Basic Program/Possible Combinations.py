"""Python Program to Accept Three Digits and Print all Possible Combinations from the Digits"""

from itertools import permutations

count = 0
list1 = list(input().split())

perm = permutations(list1)

for i in perm:
    print(i)
    count += 1
print(count)