def factorial(num):
    factorial = 1

    if num < 0:
        print("Negative Number")
    elif num == 1 or num == 0:
        print("The factorial is 1")
    else:
        for i in range(1,num+1):
            factorial = factorial * i
        print(factorial)

n = int(input())
factorial(n)
