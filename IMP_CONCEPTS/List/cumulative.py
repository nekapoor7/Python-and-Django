#Python program to find Cumulative sum of a list
from itertools import accumulate

list1 = list(map(int,input().split()))

print(list(accumulate(list1)))