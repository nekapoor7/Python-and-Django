class ContextManager():
    def __init__(self):
        print("init method called")

    def __enter__(self):
        print("enter method called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit method called")

with ContextManager() as manager:
    print("with statement block")