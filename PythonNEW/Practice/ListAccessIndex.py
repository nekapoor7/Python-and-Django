"""Write a Python program access the index of a list."""

l = list(input().split())
for num_index,num_value in enumerate(l):
    print(num_index,num_value)