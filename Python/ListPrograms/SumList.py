"""Write a Python program to sum all the items in a list"""
from functools import reduce
list1 = list(map(int,input().split()))
total = reduce(lambda x,y: x + y,list1)

print(total)


"""Write a Python program to sum all the items in a list with type string"""
list2 = list(input().split())
total = sum(int(i) for i in list2)

print(total)

