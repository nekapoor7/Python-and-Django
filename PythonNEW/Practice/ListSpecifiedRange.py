""" Write a Python program to count the number of elements in a list within a specified range."""

s,e = list(map(int,input().split()))
l = []
for i in range(s,e+1):
    l.append(i)
print(l)
print(len(l))