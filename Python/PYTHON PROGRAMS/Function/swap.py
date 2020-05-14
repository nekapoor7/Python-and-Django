#Swap of 2 numbers

def swap(x,y):
    x = x + y
    y = x - y
    x = x - y
    return x , y

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number "))
print(swap(num1,num2))
