'''This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B). '''


from itertools import product

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for i in product(list1,list2):
    print(i,end=' ')