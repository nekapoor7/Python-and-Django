"""Python Program to Sort the List According to the Second Element in Sublist"""

l1 = [['A',34],['B',21],['C',26]]

var = sorted(l1,key=lambda x :x[1])

print(var)

"""Python Program to calculate the sum of a nested list"""

l = [[1,4,3], [2,2,4], [3,1,5]]
L2 = [['a', 10, 30], ['b', 34, 89], ['c', 40, 60],['d',30,20]]

import itertools
print(sum(itertools.chain(*l)))
print(list(map(sum,zip(*l))))

from statistics import mean
Var= [mean(subl[1:]) for subl in L2]
print(Var)


"""Calculate the sum if we have blank in a list"""

def rsum(L):
    if type(L) != list:
        return L
    if L == []:
        return 0
    return rsum(L[0]) + rsum(L[1:])

L = [[1], [2, [3]], []]
print(rsum(L))




