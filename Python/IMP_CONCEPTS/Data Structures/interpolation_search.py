def interpolation_search(list1,key):
    low = 0
    high = len(list1) - 1

    while low <= high and list1[low] >= low and list1[high] <= high:
        mid = low + ((key - list1[low]/list1[high] - list1[low]) * (high - low))

        if list1[mid] == key:
            return "Key is found"
        if list1[mid] < key:
            low = mid + 1
    return "key is not found"


N = int(input())
list1 = list(map(int,input().split()))
list1.sort()
key_value = int(input())
print(interpolation_search(list1,key_value))
print(list1)