#Python | Program to print duplicates from a list of integers

list1 = list(map(int,input().split()))

new_list = sorted(set(list1))
dup_list = []

for i in range(len(new_list)):
    if list1.count(new_list[i]) > 1:
        dup_list.append(new_list[i])

print(dup_list)
