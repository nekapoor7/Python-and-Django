def binary_search(list1,key):
    low = 0
    high = len(list1)

    if len(list1) == 0:
        return False

    while low <= high:
        mid = (low+high) // 2

        if list1[mid] == key:
            return True
        elif key < list1[mid]:
            if mid - 1 < 0:
                high = mid - 1
            else:
                high = float("-inf")
        elif key > list1[mid]:
            if mid + 1 > len(list1):
                low = mid + 1
            else:
                low = float("inf")

    return False

list1 = list(map(int,input().split()))
list1.sort()
key = int(input())
print(binary_search(list1,key))