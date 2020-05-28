""" Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]"""

from itertools import zip_longest,tee,chain
def change_position(l):
    l1,l2 = tee(iter(l),2)
    return list(chain.from_iterable(zip_longest(l[1::2],l[::2])))

l = list(map(int,input().split()))
print(change_position(l))