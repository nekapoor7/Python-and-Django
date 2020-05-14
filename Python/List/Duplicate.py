"""Python Program to Remove the Duplicate Items from a List"""

list1 = list(map(int,input().split()))
removal = list(set(list1))

print(removal)