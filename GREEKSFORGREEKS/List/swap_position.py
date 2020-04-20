#Python3 program to swap elements
# at given positions

def swapElement(list,pos1,pos2):

    list[pos1],list[pos2] = list[pos2] , list[pos1]
    return list1

list1 = list(map(int,input().split()))
pos1 = int(input())
pos2 = int(input())
print(swapElement(list1,pos1,pos2))