""" Write a python program to check whether two lists are circularly identical. """
import difflib
def circular(l1,l2):
    sm = difflib.SequenceMatcher(None,l[0],l[1]*2)
    a,b,s = sm.get_matching_blocks()[0]
    return s == len(l1)

l = (['E', 'A', None, 'D', 'B', None, None, 'C'], ['B', None, None, 'C', 'E', 'A', None, 'D'])
print(circular(*l))

def Circular_identical(l1,l2):
    return (''.join(map(str,l2)) in ''.join(map(str,l1*2)))

l1 = list(input().split())
l2 = list(input().split())
print(Circular_identical(l1,l2))
