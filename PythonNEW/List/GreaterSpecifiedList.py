"""Write a Python program to find all the values in a list are greater than a specified number."""

l = list(map(int,input().split()))
N = int(input())
l1 = []
for i in l:
    if i > N:
        l1.append(i)
print(l1)