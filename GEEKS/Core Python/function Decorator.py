"""Function Decorator"""

"""A decorator function is a function that accepts a function as a parameter and returns a function.

A decorator takes the result of a function. modifies the result and returns it.

In decorators, functions are taken as the arguments into another function and  then called inside the wrapper function.

We use @function_name to specify a decorator to be applied on another function.

"""

def factorial_number(s):
    def helper(x):
            if x > 0  and type(x) == int:
                return s(x)
            else:
                raise Exception("Argument is not an Integer and Negative")
    return helper

@factorial_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int (input())
#for i in range(1,10):
print(factorial(num))


'''Property Decorator will provide an extra behaviour to my function and make it act like an attribute to my class.
  
  '''

class Games:

    def __init__(self):
        self.win = 0
        self.loss = 0

    def win_level(self):
        self.win +=1

    def loss_level(self):
        self.loss +=1

    @property
    def scores(self):
        return self.win - self.loss

g = Games()
g.win_level()
g.loss_level()
