def Genrate_function():
    yield 1
    yield 2
    yield 3

#Calling genrator object in a for loop
for value in Genrate_function():
    print(value)


