#Python program to print all odd numbers in a range

start , end = int(input()) , int(input())
list1=[]

for i in range(start,end + 1):
    if i % 2 != 0 :
        list1.append(i)

print(list1)