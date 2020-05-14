"""Write a Python program access the index of a list."""

nums = list(input().split())
for nums_index,nums_value in enumerate(nums):
    print(nums_index,nums_value)