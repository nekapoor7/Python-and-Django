#Python program to find smallest number in a list

def Bubble_sort(list1):

    for i in range(0,len(list1)-1):
        for j in range(0,len(list1)-1-i):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

list1 = list(map(int,input().split()))
Bubble_sort(list1)
print(list1)
print(list1[-1])
print(list1[-2])


#Time Complexity is O(n^2)

