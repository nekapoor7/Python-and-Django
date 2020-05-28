"""Write a Python program to check a list is empty or not."""

l = list(input().split())
for i in l:
    if len(i) > 0:
        print(l)
    else:
        print("List Empty")