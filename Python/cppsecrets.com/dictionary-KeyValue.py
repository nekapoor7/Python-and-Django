"""Python Program to Add a Key-Value Pair to the Dictionary"""

d = {}
N = int(input())

for i in range(N):
    key = input()
    value = input()
    d.update({key:value})

print(d)