""" Write a Python program to find the list of words that are longer than n from a given list of words. """

l = list(input().split())
N = int(input())
for i in l:
    if len(i) > N:
        print(i,end=' ')