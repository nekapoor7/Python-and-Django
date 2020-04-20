def Generator_object():
    yield 1
    yield 2
    yield 3

#Create a generator object
x = Generator_object()

# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())
print(x.__next__())