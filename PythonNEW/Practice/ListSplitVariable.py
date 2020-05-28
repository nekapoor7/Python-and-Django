"""Write a Python program to split a list into different variables."""

l = list(input().split())
N = int(input())
l1 = l[:N]
l2 = l[N+1:]
print(l1)
print(l2)