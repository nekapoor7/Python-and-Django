#Python | Sort the values of first list using second list

list1 = list(map(str,input().split()))
list2 = list(map(int,input().split()))

list3 = [x for _,x in sorted(zip(list2,list1))]
print(list3)