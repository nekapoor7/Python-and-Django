"""Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List"""

import random

limit = int(input())
list1 = []

for i in range(limit):
    list1.append(random.randint(1,20))

print(list1)