"""Write a Python program to generate all sublists of a list."""

def sublist(l,start,end):
    return [l[m:n+1] for m in range(start,end+1) for n in range(m,end+1)]

l = [ 44, 55, 66, 77, 88, 99, 11, 22, 33 ]
start,end = list(map(int,input().split()))
print(sublist(l,start,end))