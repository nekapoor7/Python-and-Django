"""Python Program to Find the Sum of Elements in a List Recursively"""


list1 = list(map(int,input().split()))

value = sum(sum(x) if isinstance(x,list) else x for x in list1)

print(value)