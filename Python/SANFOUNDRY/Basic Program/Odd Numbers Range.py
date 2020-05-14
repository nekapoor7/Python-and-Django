"""Python Program to Print Odd Numbers Within a Given Range"""

start , end = list(map(int,input().split()))

for i in range(start,end+1):
    if i % 2 != 0:
        print(i,end=' ')