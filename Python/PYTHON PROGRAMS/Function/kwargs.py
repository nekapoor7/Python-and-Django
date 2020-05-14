# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFunc(**kwargs):
    for key , value in kwargs.items():
        print("%s : %s" % (key, value))

myFunc(first = 'Geek' , mid = 'For' , last='Geek')