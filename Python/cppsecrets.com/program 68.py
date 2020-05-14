"""Python Program to Find the Sum of Digits in a Number without Recursion"""

num = int(input())

digsum = sum(map(int,str(num)))

print(digsum)