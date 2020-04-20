def merge_sort_divide(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort_divide(left_list)
        merge_sort_divide(right_list)
        i = 0
        j = 0
        k = 0
        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1
            k = k + 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1


N = int(input())
list1 = list(map(int,input().split()))
merge_sort_divide(list1)
print(list1)
print(list1[::-1])