"""Write a Python program to remove the K'th element from a given list, print the new list."""
def Remove(l,N):
    return l[:N-1] + l[N:]

l =list(input().split())
N = int(input())
print(Remove(l,N))

