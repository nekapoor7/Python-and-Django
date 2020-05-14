"""Python Program to Find the Largest Number in a List"""

list1 = list(map(int,input().split()))

large = list1[::-1]
print(large)
print(large[0])
print(large[1])

print(large[-1])
print(large[-2])

"""Python Program to Swap the First and Last Value of a List"""

new_list = list1[-1:] + list1[1:-1] + list1[:1]
print(new_list)

