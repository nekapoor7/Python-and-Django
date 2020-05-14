"""
Rotate the list by right by the given integer
input1 : [1,2,3,4,5], 2 -> [4,5,1,2,3]
input2 : [1,2,3,0,3], 2 -> [0,3,1,2,3]
"""

def Rotate_list(list1,val):
    list1[:] = list1[-val:] + list1[:-val]

list1 = list(map(int,input().split()))
val = int(input())
Rotate_list(list1,val)

print(list1)