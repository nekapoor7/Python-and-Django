import collections

list1 = list(map(int,input().split()))

occur = collections.Counter(list1)

dict1 = dict(occur)
print(dict1)

keymax = max(dict1,key=dict1.get)

print(keymax)