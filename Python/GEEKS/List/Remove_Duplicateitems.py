"""Remove duplicates elements from a list in Python"""

list1 = list(map(int,input().split()))

list2 = list(set(list1))

print(list2)

