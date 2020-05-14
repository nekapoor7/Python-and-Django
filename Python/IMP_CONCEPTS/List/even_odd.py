'''Python program to print even numbers in a list

Python program to print odd numbers in a List
Python program to count Even and Odd numbers in a List
Python program to print positive numbers in a list
Python program to print negative numbers in a list
Python program to count positive and negative numbers in a list
'''

list1 = list(map(int,input().split()))
count, count1,count2,count3 = 0,0,0,0

even_list = list(filter(lambda x : x % 2 ==0,list1))
for i in even_list:
    count = count + 1
print(count)

odd_list = list(filter(lambda Varx : Varx % 2 != 0 and Varx > 0,list1))
for i in odd_list:
    count1 = count1 + 1
print(count1)

positive_list = list(filter(lambda Varx : Varx < 0,list1))
for i in positive_list:
    count2 = count2 + 1
print(count2)

negative_list = list(filter(lambda VarX : VarX > 0,list1))
for i in negative_list:
    count3 = count3 + 1
print(count3)

print(even_list)
print(odd_list)
print(positive_list)
print(negative_list)