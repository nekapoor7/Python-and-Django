"""Write a Python program to insert an element at a specified position into a given list."""

l = list(map(int,input().split()))
pos = int(input())
ele = int(input())
b = l[:pos-1] +[ele] +l[pos-1:]
print(b)
