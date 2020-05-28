"""Write a Python program to iterate over two lists simultaneously."""

l1 = list(input().split())
l2 = list(input().split())

for l1,l2 in zip(l1,l2):
    print(l1,l2)