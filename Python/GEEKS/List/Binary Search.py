"""Python | Ways to check if element exists in list"""
pos = -1
def binary_search(list1,key):
    ll = 0
    ul = len(list1)-1
    while ll <= ul :
        mid = (ll + ul) // 2

        if list1[mid] == key:
            globals()['pos'] = mid
            return True
        else:
            if list1[mid] < key:
                ll = mid
            else:
                ul = mid

list1 = list(map(int,input().split()))
key = int(input())

if binary_search(list1,key):
    print("Found",pos+1)
else:
    print("Not Found")






