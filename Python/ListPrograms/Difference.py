"""Write a Python program to get the difference between the two lists."""

list1 = list(input().split())
print(list1)
list2 = list(input().split())
print(list2)
setA = set(map(int,list1))
setB = set(map(int,list2))
diff = setA.difference(setB)

print(diff)