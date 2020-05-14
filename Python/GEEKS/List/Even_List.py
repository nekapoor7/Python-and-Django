"""Python program to print even numbers in a list"""

list1 = list(map(int,input().split()))

even_list = list(filter(lambda x : x % 2 == 0 and x > 0,list1))

print(even_list)
print(len(even_list))

"""Python program to print odd numbers in a List"""

odd_list = list(filter(lambda x : x % 2 != 0,list1))

print(odd_list)
print(len(odd_list))

"""Python program to print positive numbers in a list"""

positive_list = list(filter(lambda x : x < 0 , list1))

print(positive_list)
print(len(positive_list))

"""Python program to print negative numbers in a list"""

negative_list = list(filter(lambda x : x > 0 ,list1))

print(negative_list)
print(len(negative_list))

"""Python program to print all even numbers in a range"""

lower,upper = list(map(int,input().split()))
list2 = []
list3 = []

for i in range(lower,upper + 1):
    if i % 2 == 0:
        list2.append(i)

print(list2)

"""Python program to print all odd numbers in a range"""

for i in range(lower,upper + 1):
    if i % 2 != 0:
        list3.append(i)

print(list3)
