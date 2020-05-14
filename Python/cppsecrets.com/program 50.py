"""Python Program to Find the Largest Number in a List"""

list1 = list(map(int,input().split()))

largest = max(x for x in list1 if x == max(list1))

print(largest)