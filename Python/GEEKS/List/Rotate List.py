"""Rotating values in a list [Python]"""

def rotate(list1,n):
    list1[:] = list1[-n:] + list1[:-n]

list1 = list(map(int,input().split()))
n = int(input())
rotate(list1,n)

print(list1)

