"""Actual Argument : Function calls arguments are called Actual Argument.

Formal Argument: Function definition parameters are called as formal arguments.

Types of Actual Arguments
1. Positional Argument : These arguments are passed to the function in correct positional order.
 The number of arguments and their positions in the function definition should be equal to the number
 and position of the argument in the function call.
2. Keyword Argument: These arguments are passed to the function with name-value pair so keyword arguments can identify
the formal arguments by their names. The keyword argument's name and formal argument's name must match.
3. Default Argument
4. variable Length Argument
5. Keyword Variable Length Argument

"""
"""----> Formal Argument"""
def add(x,y):
    c = x + y
    return c

print(add(10,20))
#Actual Argument

"""Keyword Arguments 

def show (name,age):
    print(name,age)
    
    show(name="neha",age=30)
    show(age=33,name="harsh")
    
Default Arguments : Sometimes we mention default value to the formal argument in function definition and 
we may not required to provide actual argument, in this case default argument will be used by formal argument.

If we dont provide actual argument for formal argument explicitly while calling the function then formal argument will use 
default value on the other hand if we provide actual argument then it will use provided value

def show(name,age=27) --> default Argument   

Variable Length Arguments: argument that can accept any number of values. Its written with * symbol.
It stores values in tuple.

def add(*num):
    z = num[0] + num[1] + num[2]
    print(z)
    
add(5,2,4)    

def add(x,*num):
    z = x + num[0] + num[1]
    print(z)
    
add(5,2,4)

5. Keyword Variable Length Argument: Argument that can accept any number of vakues provided in the form of key-value pair.
Its written with ** symbol. It stores all the value in a dictionary in the form of key-value pair.

def add(**num):
    z = num['a'] + num['b'] + num['c']
    print(z)
    
add(a=5,b=2,c=4)  
    
    
    

"""

