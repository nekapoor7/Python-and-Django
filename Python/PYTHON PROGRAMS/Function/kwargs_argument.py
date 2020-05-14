# Python program to illustrate  **kargs for
# variable number of keyword arguments with
# one extra argument.

def myFunc(arg1 , **kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key, value))

myFunc("Hi", first ='Geeks', mid ='for', last='Geeks')