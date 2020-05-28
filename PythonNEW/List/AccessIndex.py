""" Write a Python program access the index of a list."""

l = list(input().split())

for nums_index,nums_value in enumerate(l):
    print(nums_index,nums_value)
