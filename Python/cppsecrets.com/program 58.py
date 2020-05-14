"""Python Program to Find the Sum of the Digits of the Number Recursively"""

num = int(input())

digsum = sum(map(int,str(num)))

print(digsum)