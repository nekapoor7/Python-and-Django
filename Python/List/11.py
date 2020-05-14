""" Write a Python function that takes two lists and returns True if they have at least one common member."""

l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l1 = ['Green', 'White', 'Black']
r = False
for x in l:
    for y in l1:
        if x == y:
            r = True
print(r)

""" Write a Python program to get the difference between the two lists."""

s1 = set(l)
s2 = set(l1)
res = s1.difference(s2)
print(res)

"""Write a Python program to find common items from two lists. """
res1 = s1.intersection(s2)
print(res1)

""" Write a Python program to convert a list of characters into a string."""
s3 = ''.join(l1)
print(s3)

""" Write a Python program access the index of a list. """
for nums_index,nums_value in enumerate(l):
    print(nums_value,nums_index)

"""Write a Python program to find the index of an item in a specified list."""
n = input()
print(l.index(n))

""" Write a Python program to append a list to the second list."""
print(l1+l)
