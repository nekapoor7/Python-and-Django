"""Write a Python program to sum all the items in a list. """
l = ['1', '2', '3', '4', '5', '5', '5', '5', '56', '6', '6', '7', '7', '7', '8', '9']
s = sum(map(int,l))
print(s)

"""Write a Python program to multiplies all the items in a list."""
from functools import reduce
l1 = list(map(int,l))
print(l1)
m = reduce(lambda x , y : x * y,l1)
print(m)

""" Write a Python program to get the largest number from a list. """
m1 = max(int(x) for x in l if x == max(l))
print(m1)

"""Write a Python program to get the smallest number from a list."""
s1 = min(int(x) for x in l if x == min(l))
print(s1)

"""Write a Python program to find the second smallest number in a list."""
s2 = min(int(x) for x in l if x != min(l))
print(s2)

""" Write a Python program to find the second largest number in a list."""
s3 = max(int(x) for x in l if x != max(l))
print(s3)

"""Write a Python program to remove duplicates from a list."""
""" Write a Python program to get unique values from a list."""
setA = set(l)
print(' '.join(sorted(list(setA))))

"""Write a Python program to clone or copy a list."""
l2 = list(l1)
print(l2)

"""Write a Python program to check a list is empty or not."""
l3 = []
if len(l3) < 1:
    print("Empty")
else:
    print(l3)

""" Write a Python program to find the list of words that are longer than n from a given list of words. """
w = 3
word = ['Green', 'White', 'Black', 'Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
w1 = []
for i in word:
    if len(i) > w:
        w1.append(i)
print(w1)

""" Write a Python program to get the frequency of the elements in a list."""
from collections import Counter
occur = Counter(word)
print(occur)

"""How to sort a list alphabetically"""
print(sorted(word,key=str.lower))

""" Write a Python program to count the number of elements in a list within a specified range."""
n1,n2 = list(map(int,input().split()))
l3 = []
for i in range(n1,n2+1):
    l3.append(i)
print(l3)
print(len(l3))

""" Write a Python program to check whether a list contains a sublist."""
le=['1', '2', '3']
le1 = map(int,le)
lw=['1', '2', '3', '4', '5']
lw1 = map(int,lw)
print(all(i in lw1 for i in le1))

"""Write a Python program to generate all sublists of a list"""
def sublist(l1,i,j):
    return [l1[m:n+1] for m in range(i,j+1) for n in range(m,j+1)]

l1 = ['X','Y','Z']
i, j = list(map(int,input().split()))
print(sublist(l1,i,j))

"""Generate all possible combinations:"""
from itertools import combinations
l5 = []

for x in range(1,len(l1)+1):
    l5.extend(list(combinations(l1,x)))
print(l5)

"""Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
Sample list: [11, 33, 50]
Expected Output: 113350"""
l6 = ''.join(l)
print(l6)

"""Write a Python program to remove consecutive duplicates of a given list. Go to the editor
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]"""
from itertools import groupby
l7 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
aa = [key for key,group in groupby(l7)]
print(aa)