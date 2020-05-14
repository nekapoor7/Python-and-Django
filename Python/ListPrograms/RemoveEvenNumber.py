"""Write a Python program to print the numbers of a specified list after removing even numbers from it."""

list1 = list(input().split())
list2 = []

for i in map(int,list1):
    if i % 2 != 0:
        list2.append(i)
print(list2)