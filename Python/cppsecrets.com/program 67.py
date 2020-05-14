"""Python Program to Sort the List According to the Second Element in Sublist"""
import itertools

L = [[50, 10, 30], [45, 34, 89], [93, 40, 60],[5,30,20]]

sortlist = sorted(L,key=lambda x:x[1])

print(sortlist)