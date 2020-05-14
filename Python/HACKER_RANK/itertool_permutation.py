'''This tool returns successive

length permutations of elements in an iterable.

If
is not specified or is None, then

defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted,
 the permutation tuples will be produced in a sorted order.'''


from itertools import permutations

s = input().split()

for i in sorted(permutations(s[0],int(s[1]))):
    print(''.join(i))


