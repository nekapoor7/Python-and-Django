#Python Program to Merge Two Lists and Sort it

list1 = list(map(int,input("enter the multiple values").split()))

list2 = list(map(int,input("enter the multiple values").split()))

merge_list = [y for x in [list1,list2] for y in x]

#print(merge_list)

def bubble_sort(merge_list):
    num = len(merge_list)

    for i in range(num):
        for j in range(0,num-i-1):

            if merge_list[j] > merge_list[j+1]:
                merge_list[j] , merge_list[j+1] = merge_list[j+1],merge_list[j]

bubble_sort(merge_list)

print ("Sorted array is:")
for i in range(len(merge_list)):
    print("%d" %merge_list[i]),


def removal_duplicate(merge_list):
    final_list = []
    for num in merge_list:
        if num not in final_list:
            final_list.append(num)
    return final_list

print(removal_duplicate(merge_list))