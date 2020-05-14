import itertools

user = str(input())
user = list(user)
counter = 0


permutation = itertools.permutations(user,len(user))
for p in permutation:
    print(p)
    counter += 1
print(counter)