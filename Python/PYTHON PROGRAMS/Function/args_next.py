# Python program to illustrate
# *args with first extra argument

def myFunc(num1,*args):
    print("value of num",num1)
    for arg in args:
        print(arg)
        print("Next argument through *argv :", arg)

myFunc('Hello', 'Welcome', 'to', 'GeeksforGeeks')