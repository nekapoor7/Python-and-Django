def sum_digit(num):
    sum = 0
    while num > 0:
        remainder = num % 10
        sum = sum + remainder
        num = num // 10
    print(sum)

N = int(input())
sum_digit(N)
