from contextlib import contextmanager

@contextmanager
def ContextManager():

    print("yield method called")
    yield

    print("exit method called")

with ContextManager() as manager:
    print('with statement block')