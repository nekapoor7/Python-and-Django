'''

Rotate the list by right by the given integer
input1 : [1,2,3,4,5], 2 -> [4,5,1,2,3]
input2 : [1,2,3,0,3], 2 -> [0,3,1,2,3]

'''

l = [1,2,3,4,5]

def rotate(l,x):
    ll = l[-x:] + l[:-x]
    return ll

l = [1,2,3,4,5]
x = int(input())
print(rotate(l,x))

""" Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l[::2], l[1::2] = l[1::2], l[::2]

print(l)

"""Write a Python program to get the frequency of the elements in a list."""
from collections import Counter
l = list(map(int,input().split()))
print(l)
ll = Counter(l)
print(ll)
d = dict(ll)
print(d)
maxoccur = max(d,key=d.get)
print(maxoccur)

