"""Python Program to Find the Sum of Digits in a Number"""
"""Python Program to Count the Number of Digits in a Number"""

num = int(input())
sum = 0
count = 0

while num > 0:
    digits = num % 10
    sum = sum + digits
    num = num // 10
    count += 1

print(sum)
print(count)