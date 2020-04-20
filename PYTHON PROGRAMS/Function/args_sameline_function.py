# Now we can use both *args ,**kwargs to pass arguments to this function :

def myFunc(*args, **kwargs):
    print("args:",args)
    print("kwargs:",kwargs)

myFunc('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")