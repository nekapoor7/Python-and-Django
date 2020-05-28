"""Write a Python program to get the frequency of the elements in a list."""
from collections import Counter
l = list(input().split())
ll = Counter(l)
print(ll)

"""Find the most common element in a list"""

def most_common(l):
    return max(set(l),key=l.count)

l = [1,2,2,2,2,2,2,4,4,4,5,5,5,5]
print(most_common(l))