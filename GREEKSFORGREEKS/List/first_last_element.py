## Python3 program to swap first
# and last element of a list

def swapList(NewList):

    NewList[0],NewList[-1] = NewList[-1],NewList[0]

    return NewList

list1 = list(map(int,input().split()))
print(swapList(list1))