a = 1

def f():
    print("Inside function f()",a)

def g():
    g = 2
    print("Print value Inside g()",a)

def h():
    global a
    a = 3
    print("Print value inside h()",a)

#Global scope
print('global : ',a)
f()
print('global : ',a)
g()
print('global : ',a)
h()
print('global : ',a)
