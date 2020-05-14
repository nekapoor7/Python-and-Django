"""Python program to find sum of elements in list"""

list1 = list(map(int,input().split()))
sum = 0

for i in list1:
    sum += i
print(sum)