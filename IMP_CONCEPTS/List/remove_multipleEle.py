#Remove multiple elements from a list in Python

list1 = list(map(int,input().split()))

remove_list = list(map(int,input().split()))

result = list(set(list1).difference(set(remove_list)))

print(result)