"""Python program to check largest number of three numbers"""

list1 = list(map(int,input().split()))

largest = max(x for x in list1 if x == max(list1))

print(largest)