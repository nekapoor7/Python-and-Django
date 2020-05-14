"""Python Program to Find the Length of a List Using Recursion"""
import re

list1 = list(map(int,input().split()))

LL = str(list1)
print(LL)

LL1 = re.findall(r'[0-9]+',LL)

print(len(LL1))