## class Error is derived from super class Exception

class MyError(Exception):
    pass

class TransitionError(Exception):

    def __init__(self,prev,next,msg):
        self.prev = prev
        self.next = next
        self.msg = msg

try:
    raise(TransitionError(2,3*2,"Not Allowed"))
except TransitionError as error:
    print('Exception occured: ', error.msg)
