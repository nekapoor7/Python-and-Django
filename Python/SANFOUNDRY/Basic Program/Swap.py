"""Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable"""

num1, num2 = list(map(int,input().split()))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(num1)
print(num2)