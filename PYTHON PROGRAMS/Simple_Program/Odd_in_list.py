#Python Program to Print Odd Numbers Within a Given Range
import itertools

list1 = list(int(num) for num in input("Enter the multiple values").strip().split())

'''odd_list = list(filter(lambda x: (x % 2 != 0), list1))

even_list = list(filter(lambda x: (x % 2 == 0), list1))

print(odd_list)

print(even_list)'''

'''odd_list = list(itertools.filterfalse(lambda x : x % 2 == 0,list1))

even_list = list(itertools.filterfalse(lambda x : x % 2 != 0,list1))

print(odd_list)

print(even_list)'''