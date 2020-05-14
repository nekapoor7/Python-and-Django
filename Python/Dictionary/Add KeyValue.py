"""Python Program to Add a Key-Value Pair to the Dictionary"""

dict1 = {}
limit = int(input())

for i in range(limit):
    key = input()
    value = input()
    dict1.update({key:value})

print(dict1)