"""Write a Python program to check whether the n-th element exists in a given list. """

l = list(input().split())
l = map(int,l)
N = int(input())

if N in l:
    print("ele exist")
else:
    print("ele not exist")