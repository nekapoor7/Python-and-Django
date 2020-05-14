#Python program to print positive numbers in a list

list1 = list(map(int,input().split()))
count , count1 = 0 , 0

positive_list = list(filter(lambda varX : varX > 0 , list1))
for i in positive_list:
    count += 1

odd_list = list(filter(lambda varX : varX < 0 , list1))
for i in odd_list:
    count1 += 1

print(positive_list)
print(count)


print(odd_list)
print(count1)