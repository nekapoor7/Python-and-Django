# Python program to illustrate
# *args for variable number of arguments

def myFunc(*args):
    for arg in args:
        print(arg)

myFunc('Hello', 'Welcome', 'to', 'GeeksforGeeks')