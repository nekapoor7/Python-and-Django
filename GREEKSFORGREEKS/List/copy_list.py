#Python | Cloning or Copying a list

def cloneCopy(list1):
    list1_copy = [ i for i in list1]
    return list1_copy


list1 = list(map(int,input().split()))
list2 = cloneCopy(list1)
#print(list1)
print(list2)


