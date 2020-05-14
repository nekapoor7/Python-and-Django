"""Python Program to Print Odd Numbers Within a Given Range"""

lower,upper = list(map(int,input().split()))
list1 = []

for i in range(lower,upper + 1):
    if i % 2 != 0:
        list1.append(i)

print(list1)