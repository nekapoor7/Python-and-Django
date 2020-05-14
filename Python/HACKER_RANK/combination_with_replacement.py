from itertools import combinations_with_replacement

S,k = input().split()

l = combinations_with_replacement(sorted(S),int(k))
print(*[''.join(i) for i in l],sep='\n')