"""Python Program to Put Even and Odd elements in a List into Two Different Lists"""

list1 = list(map(int,input().split()))

even_list = list(filter(lambda Varx : Varx % 2 == 0,list1))

odd_list = list(filter(lambda Vary : Vary % 2 != 0,list1))

print(even_list)

print(odd_list)