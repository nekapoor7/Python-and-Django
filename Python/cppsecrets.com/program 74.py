"""Python Program to Find the Second Largest Number in a List Using Bubble Sort"""

list1 = list(map(int,input().split()))
secnum = max(ele for ele in list1 if ele != max(list1))

print(secnum)