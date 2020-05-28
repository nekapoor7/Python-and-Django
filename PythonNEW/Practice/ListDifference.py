"""Write a Python program to get the difference between the two lists."""

l = list(input().split())
l1 = list(input().split())

diff = list(set(l).difference(set(l1)))
print(diff)