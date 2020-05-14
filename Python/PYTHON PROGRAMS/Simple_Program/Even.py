#Python Program to Check Whether a Number is Positive or Negative
from functools import reduce

num = int(input("Enter the number"))

'''even_num = lambda num: num%2 == 0

odd_num = lambda num: num%2 != 0


print("Even number",even_num)

print("Odd number", odd_num)

print("Even Number")
else:
    print("Odd Number")'''

if num%2 == 0:
    print("Even number")
else:
    print("Odd Number")