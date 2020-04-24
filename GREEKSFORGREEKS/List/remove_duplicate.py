#Python Remove Duplicates from a List
#Python | Program to print duplicates from a list of integers

list1 = list(map(int,input().split()))
list2 = []
#new_list = list(set(list1))

[list2.append(x) for x in list1 if x in list2]
print(list2)



#print(new_list)