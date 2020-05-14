def binary_search(list1,key):
    low = 0
    high = len(list1)-1
    found = False
    while low<=high and not found:
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid -1
    if found is True:
        print("key is found")
    else:
        print("key is not found")


N = int(input())
list1 = list(map(int,input().split()))
list1.sort()
key_value = int(input())
binary_search(list1,key_value)
print(list1)

