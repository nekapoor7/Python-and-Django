"""Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336 """
from functools import reduce


def multiplylist(l):
    m = reduce(lambda x,y:x*y,l)
    return m

l = list(map(int,input().split()))
print(multiplylist(l))