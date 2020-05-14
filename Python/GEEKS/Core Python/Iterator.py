"""Python Iterator

An iterator is an object that contains a specific number of objects that are countable and it is basically used to iterate
over a sequence which means we can go through each value in a collection and iterator in python implements the iterator
protocol which means it implement the methods __iter__ and __next__.

Difference between Iterator and Iterable

Iterable is an object, which one can iterate upon. It generates an iterator when passed to iter() method.
iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterator have __next__()
method, which returns the next item of an object.

Every iterator is an iterable but not every iterable is an iterator. An iterator can be created from an iterable by
using the function iter(). to make this possible, the class of an objects needs either a method __iter__,which returns
an iterator or a __getitem__ method with sequential indexes starting from 0.

1. __iter__ method is called on initialization of an iterator. this should return an object that has __next__ method.

2. __next__ : The iterator next method should return the next value for the iterable.

"""

# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))


# An iterable user defined type
class Test:

    # Cosntructor
    def __init__(self, limit):
        self.limit = limit

        # Called when iteration is initialized

    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def next(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

            # Else increment and return old value
        self.x = x + 1;
        return x

    # Prints numbers from 10 to 15


for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)