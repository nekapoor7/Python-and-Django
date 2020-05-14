def g():
    print("This is Python Program")
    print("PYTHON")

def f(func):
    print("My name is Neha")
    print("Kapoor")
    func()
    print("func's real name is " + func.__name__)

f(g)