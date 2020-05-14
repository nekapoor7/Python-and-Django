"""Python program to check particular char is in list or not"""

from collections import Counter

list1 = list(map(str,input().split()))

print(list1)

char = input()

if char in list1:
    print("Char is present")
else:
    print("Char is not present")