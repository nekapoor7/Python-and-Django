""" Write a Python function that takes two lists and returns True if they have at least one common member."""

l = list(input().split())
l1 = list(input().split())
result = False
for i in l:
    for j in l1:
        if i == j:
            result = True
            print(result)