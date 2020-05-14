"""Pass/Call by Object Reference"""

'''When we pass value like number,strings,tuples or lists to function, the references of these objects are 
passed to function.'''

def val(x):
    x = 15
    print(x,id(x))

x = 10
val(x)
print(x,id(x))

'''An object created in a memory with 10 and assign address, when it moves to x = 15.
A new object is created in memory because integer objects are immutable (not modifiable).'''

""" Object by Reference for List"""

def val(lst):
    lst.append(4)
    print(lst,id(lst))


lst = [1,2,3]
print(lst,id(lst))
val(lst)
print(lst,id(lst))

"""It will create a list=lst[1,2,3] when it will read val it will append list = lst[1,2,3,4]
When it will append the list it will not create new list it will just append the list and it will 
point to the same list address."""

A = sorted(list([4,5,3,2,1]))
print(A)

'''A new object is not created in the memory because list objects are mutable(modifiable).it simply add new element
to the same object.'''
