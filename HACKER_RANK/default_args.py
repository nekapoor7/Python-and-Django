'''Python supports a useful concept of default argument values. For each keyword argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it. For example, consider the following increment function:

def increment_by(n, increment=1):
    return n + increment

The functions works like this:

>>> increment_by(5, 2)
7
>>> increment_by(4)
5
>>>'''
