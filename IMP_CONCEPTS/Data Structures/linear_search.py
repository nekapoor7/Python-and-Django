def linear_search(list1,key):
    for i in range(0,len(list1)):
        if key == list1[i]:
            return "Key Found"
            break
    else:
        return "Key Not found"

N = int(input())
list1 = list(map(int,input().split()))
key = int(input())
print(linear_search(list1,key))

