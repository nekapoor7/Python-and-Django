"""Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List"""

list1 = list(map(int,input().split()))

neg_num = sum(list(filter(lambda varx : varx < 0,list1)))

pos_num = sum(list(filter(lambda varx : varx > 0 and varx % 2 == 0,list1)))

odd_num = sum(list(filter(lambda varx : varx > 0 and varx % 2 != 0,list1)))

print(neg_num)

print(pos_num)

print(odd_num)