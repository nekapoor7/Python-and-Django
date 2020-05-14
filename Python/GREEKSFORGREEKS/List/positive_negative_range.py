'''Python program to print all positive numbers in a range
Python program to print all negative numbers in a range'''

start , end = int(input()), int(input())
list1 = []
list2 = []

for i in range(start,end + 1):
    if i % 2 == 0:
        list1.append(i)
    else:
        list2.append(i)
print(list2)
print("Positive Range",list1)