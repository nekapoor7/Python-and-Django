#Python program to print even numbers in a list

list1 = list(map(int,input().split()))
count , count1 = 0 , 0

list_Even_Numbers = list(filter(lambda varX: varX % 2 == 0,list1))
for i in list_Even_Numbers:
    count += 1

list_Odd_Numbers = list(filter(lambda varX: varX % 2 == 1,list1))
for i in list_Odd_Numbers:
    count1 += 1


print(list_Even_Numbers)
print(count)

print(list_Odd_Numbers)
print(count1)