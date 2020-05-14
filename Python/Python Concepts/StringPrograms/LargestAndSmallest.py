"""Write a Python program to find smallest and largest word in a given string."""

words = list(input().split())
minle = min(len(x) for x in words)
maxle = max(len(x) for x in words)

l1 = [x for x in words if len(x) == minle]
l2 = [x for x in words if len(x) == maxle]
print(l1,l2)
s1 = ''.join(l1)
s2 = ''.join(l2)

print(s1,len(s1),s2,len(s2))