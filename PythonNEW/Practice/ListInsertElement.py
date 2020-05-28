"""Write a Python program to insert an element at a specified position into a given list. Go to the editor"""

l = list(input().split())
N = int(input())
pos = int(input())

ll = l[:pos] +[N] + l[pos + 1:]
print(ll)