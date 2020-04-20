# Python program to find second largest
# number in a list

list1 = list(map(int,input().split()))

new_list = set(list1)

new_list.remove(max(new_list))

print(max(new_list))