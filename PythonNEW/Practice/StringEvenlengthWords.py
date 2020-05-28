"""Python program to print even length words in a string"""
import re
s = input().split()
for word in s:
    if len(word) % 2 == 0:
        print(word,end=' ')