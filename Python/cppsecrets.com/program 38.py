"""Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers"""

lower,upper = list(map(int,input().split()))
list1 = []

for x in range(lower,upper + 1):
    if x % 7 == 0 and x % 5 == 0:
        list1.append(x)

print(list1)


