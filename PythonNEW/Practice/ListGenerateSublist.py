""" Write a Python program to generate all sublists of a list."""

l = [1,2,3,4,5,6,7,8]
N = int(input())
ll = [l[i:i+N] for i in range(0,len(l),N)]
print(ll)