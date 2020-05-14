"""Python Program to Search the Number of Times a Particular Number Occurs in a List"""

from collections import Counter

list1 = list(map(int,input().split()))

occur = Counter(list1)

print(occur)