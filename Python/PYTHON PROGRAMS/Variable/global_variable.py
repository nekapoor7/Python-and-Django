"""Global Variable

When a variable is declared above function,it becomes global variable. These variables are avaible to all the functions
which are writen after it. The scope of global variable is the entire program."""


def f():
    global s
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)

s = "Global Variable"
f()
print(s)
