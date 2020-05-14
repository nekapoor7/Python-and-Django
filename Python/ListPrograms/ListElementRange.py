""" Write a Python program to count the number of elements in a list within a specified range."""

start,end = list(map(int,input().split()))
list1 = []

for i in range(start,end+1):
    list1.append(i)
print(list1)