"""Python Program to Merge Two Lists and Sort it"""

from itertools import chain

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

result = list(set(chain(*zip(list1,list2))))

print(result)