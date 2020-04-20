## Program to depict else clause with try-except

def computeABC(x,y):
    try :
        c = ((x+y)/(x-y))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
computeABC(num1,num2)