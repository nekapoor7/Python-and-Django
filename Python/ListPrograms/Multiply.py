"""Write a Python program to multiplies all the items in a list."""

from functools import reduce
'''
list1 = list(map(int,input().split()))
multiply = reduce(lambda x , y : x * y,list1)
print(multiply)'''

list2 = list(input().split())
l = ' '.join(list2)
mult = reduce(lambda x , y: x * y,l)
print(mult)