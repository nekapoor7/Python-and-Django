#Python code to illustrate
# clean up actions

def divide(x,y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        print("I'm finally clause, always raised !! ")

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
divide(num1,num2)