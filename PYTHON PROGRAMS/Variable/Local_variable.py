"""Local Variables

The variable which are declared inside a function called as Local variable. Local variable scope is limited
only to that function where it is created. It means local variable value is available only in that function
not outside of that function.

"""
'''
def add(y):
    x = 10          """ --> Local variable """
    print(x)           ---> using local variable inside Function
    print(x + y)
add(20)
print(x)   """---> Using local Variable Outside function, it will show error"""'''