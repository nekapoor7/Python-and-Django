# Python program to find second minimum
# number in a list

list1 = list(map(int,input().split()))

new_list = set(list1)

new_list.remove(min(new_list))

print(min(new_list))