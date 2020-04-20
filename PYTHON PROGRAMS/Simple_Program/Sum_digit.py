#Python Program to Find the Sum of Digits in a Number

num = int(input("Enter the number"))
sum = 0

while (num > 0):
    dig = num % 10
    sum = sum + dig
    num = num // 10
print(sum)