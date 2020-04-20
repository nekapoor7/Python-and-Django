'''This tool returns the

length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.'''


from itertools import combinations

S,k = (input().split())
for i in range(1,int(k)+1):
    l=list(combinations(sorted(S),i))
    # l.sort()
    print(*[''.join(j) for j in l],sep="\n")