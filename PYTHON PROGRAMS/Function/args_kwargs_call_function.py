# Now we can use *args or **kwargs to
# pass arguments to this function :

def myFunc(arg1,arg2,arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("Geeks", "for", "Geeks")
myFunc(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFunc(**kwargs)