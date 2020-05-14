"""Python Program to Swap the First and Last Value of a List"""

list1 = list(map(int,input().split()))
list2 = []

list2 = list1[-1:]+list1[1:-1]+list1[:1]
print(list2)