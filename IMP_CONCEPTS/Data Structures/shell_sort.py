def shell_sort(list1):
    gap = len(list1)//2
    while gap > 0:
        for index in range(gap,len(list1)):
            current_element = list1[index]
            pos = index
            while current_element < list1[pos-gap] and pos >= gap:
                list1[pos] = list1[pos-gap]
                pos = pos - gap
            list1[pos] = current_element
        gap = gap // 2

N = int(input())
list1 = list(map(int,input().split()))
shell_sort(list1)
print(list1)