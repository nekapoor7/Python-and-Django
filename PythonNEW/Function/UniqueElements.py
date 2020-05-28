"""Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]"""

def unique(l):
    s = set(l)
    return list(s)

l = list(map(int,input().split()))
print(unique(l))