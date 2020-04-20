'''You are given a function . You are also given lists. The list consists of

elements.

You have to pick one element from each list so that the value from the equation below is maximized:

% denotes the element picked from the list . Find the maximized value

obtained.

denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element.
 You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain,
 will be the answer to the problem. '''

import itertools

(K, N) = map(int, input().strip().split(' '))

# reading the K lines and appending lists to 'L'
L = list()
for i in range(K):
    l = list(map(int, input().strip().split(' ')))
    n = l[0]
    L.append(l[1:])
    assert len(L[i]) == n

S_max = 0
L_max = None

# Looping through Cartesian product of list and getting max sum.
for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print(S_max)