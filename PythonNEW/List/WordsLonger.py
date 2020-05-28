"""Write a Python program to find the list of words that are longer than n from a given list of words."""

def longer(l,N):
    l1 = []
    for i in l:
        if len(i) > N:
            l1.append(i)
    return l1

l = list(input().split())
N = int(input())
print(longer(l,N))