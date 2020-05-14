num = int(input())
factorial = 1

if num < 0 :
    print("Negative Number")
elif num == 0 or num == 1:
    print("factorial is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(factorial)