#Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2


print(num1)
print(num2)