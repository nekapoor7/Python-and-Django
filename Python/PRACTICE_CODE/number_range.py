#Python Program to Print all Numbers in a Range Divisible by a Given Number

def range_divisible(num1,num2,n):
    list1 = []
    sum = 0
    for i in range(num1,num2 +1):
        if i % n == 0:
            list1.append(i)
            sum += i
    print(list1)
    print(sum)
    max_num = list1[0]
    for num in list1:
        if max_num < num:
            max_num = num
    print(num)

num1 , num2 = list(map(int,input().split()))
number = int(input())
range_divisible(num1,num2,number)