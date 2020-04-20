def insertion_sort(list1):
    for index in range(1,len(list1)):
        current_value = list1[index]
        pos = index
        while current_value < list1[pos-1] and pos > 0:
            list1[pos] = list1[pos-1]
            pos = pos -1
        list1[pos] = current_value

N = int(input())
list1 = list(map(int,input().split()))
insertion_sort(list1)
print(list1)
print(list1[::-1])


