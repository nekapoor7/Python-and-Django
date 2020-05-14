#Selection Sort

def selection_sort(list1):
    for i in range(len(list1)):
        min_val = min(list1[i:])
        min_index = list1.index(min_val,i)
        list1[i],list1[min_index] = list1[min_index],list1[i]

list1 = list(map(int,input().split()))
selection_sort(list1)

print(list1)