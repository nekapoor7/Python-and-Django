"""How to remove multiple indexes from a list at the same time"""

list1 = list(map(int,input().split()))
list2 = set(map(int,input().split()))
list3 = []

list3 = [v for i, v in enumerate(list1) if i not in list2]
print(list3)