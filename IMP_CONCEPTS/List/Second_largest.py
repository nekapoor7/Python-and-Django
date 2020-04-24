#Python program to find second largest number in a list

def selection_sort(list1):

    for i in range(0,len(list1)):
        min_val = min(list1[i:])
        min_index = list1.index(min_val,i)
        list1[i],list1[min_index] = list1[min_index],list1[i]


list1 = list(map(int,input().split()))
selection_sort(list1)
print(list1[0])
print(list1[-1])
print(list1[-2])