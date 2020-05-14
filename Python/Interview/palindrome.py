"""# Q6. How will you check if the string is palindrome ?
input: aba, output: True
input: blah, output: False"""


def Palind(s):
    if s == s[::-1]:
        return True
    else:
        return False

s= input()
print(Palind(s))

"""# Q7.
Rotate the list by right by the given integer
input1 : [1,2,3,4,5], 2 -> [4,5,1,2,3]
input2 : [1,2,3,0,3], 2 -> [0,3,1,2,3]"""

def Rotate(l,x):
    ll = l[-x:] + l[:-x]
    return ll

l = [1,2,3,4,5]
N = int(input())
print(Rotate(l,N))

"""Q12. Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2"""
from collections import Counter
def Majority(l,N):
    m = Counter(l)
    '''d = dict(m)
    mele = max(d,key=d.get)'''
    mele = Counter(m).most_common(N)
    return mele

l1 = [2,2,1,1,1,2,2]
N = int(input())
print(Majority(l1,N))
