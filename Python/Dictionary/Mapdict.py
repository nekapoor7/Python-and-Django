"""Python Program to Map Two Lists into a Dictionary"""

list1 = list(map(str,input().split()))
list2 = list(map(str,input().split()))

d = dict(zip(list1,list2))

print(d)