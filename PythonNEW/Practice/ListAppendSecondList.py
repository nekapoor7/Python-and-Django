"""Write a Python program to append a list to the second list."""

l = list(input().split())
l1 = list(input().split())

for i in l:
    l1.append(i)
print(' '.join(l1))