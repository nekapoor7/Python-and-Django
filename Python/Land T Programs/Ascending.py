"""
Given an unsorted list of integers, sort the list in an ascending order without using any type of inbuilt sort function"

eg1. [9,4,1] -> [1,4,9]
eg2. [4,2,3] -> [2,3,4]
"""

list1 = list(map(int,input().split()))
list2 = []

list2 = list1[::-1]

print(list2)