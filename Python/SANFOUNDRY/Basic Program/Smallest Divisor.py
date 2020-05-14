"""Python Program to Find the Smallest Divisor of an Integer"""

num1,num2,div = list(map(int,input().split()))
list1 = []

for i in range(num1,num2+1):
    if i % div == 0:
        list1.append(i)
print(list1)
print(list1[0])