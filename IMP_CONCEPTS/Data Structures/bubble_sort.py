N = int(input())
list1 = list(map(int,input().split()))

for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            list1[i] , list1[i+1] = list1[i+1],list1[i]

print(list1)

print("Reverse the list",list1[::-1])
