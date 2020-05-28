""" Write a Python program to count the number of elements in a list within a specified range."""

n1,n2 = list(map(int,input().split()))
l = []
for i in range(n1,n2 +1):
    l.append(i)
print(len(l))