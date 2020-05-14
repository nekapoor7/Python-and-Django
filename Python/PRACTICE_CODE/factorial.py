#Python Program for factorial of a number

num = int(input())
factorial = 1

if num < 0:
    print("Negative number")
elif num == 0 and num == 1:
    print("Factorial of {0} and {1} is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial * i
    print(factorial)