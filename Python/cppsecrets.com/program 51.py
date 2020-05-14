"""Python Program to Find the Second Largest Number in a List"""

list1 = list(map(int,input().split()))

seclarge = max(ele for ele in list1 if ele != max(list1))

print(seclarge)