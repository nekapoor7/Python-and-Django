""" Write a Python program to find the list of words that are longer than n from a given list of words."""

range = int(input())
list1 = list(input().split())
l = []

for words in list1:
    if len(words) > range:
        l.append(words)

print(l)
