"""Selection Sort"""


def selection_sort(list1):
    for i in range(len(list1)):
        max_val = max(list1[i:])
        max_index = list1.index(max_val,i)
        list1[i],list1[max_index] = list1[max_index],list1[i]

list1 = list(map(int,input().split()))
selection_sort(list1)

print(list1)