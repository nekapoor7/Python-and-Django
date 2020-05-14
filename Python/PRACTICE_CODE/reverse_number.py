#Python Program to Reverse a Given Number

def reverse_num(num):
    digit = 0
    while num > 0:
        remainder = num % 10
        digit = digit*10 + remainder
        num = num // 10
    print(digit)

N = int(input())
reverse_num(N)