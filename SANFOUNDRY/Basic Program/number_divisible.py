"""Python Program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50."""

start,end = list(map(int,input().split()))

for i in range(start,end + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i,end= ' ')