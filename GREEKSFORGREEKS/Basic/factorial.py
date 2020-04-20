#Python Program for factorial of a number
def factorial(num):
    if num == 1: return 1
    else: return num * factorial(num-1)

num = int(input())
if num < 0 :
    print("Factorial can't Found")
elif num == 1 :
    print("Factorial is always 1")
else:
    print(factorial(num))