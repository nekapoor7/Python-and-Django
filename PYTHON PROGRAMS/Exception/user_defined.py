## A python program to create user-defined exception

class MyError(Exception):

    def __init__(self,value):
        self.value = value

    def __str__(self,value):
        return (repr(self.value))

try:
    raise(MyError(2*3))

except MyError as error:
    print('A New Exception occured: ', error.value)

