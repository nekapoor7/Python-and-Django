'''def add(num1, *args):
    total = num1
    for arg in args:
        return arg


x = int(input("number1"))
y = int(input("number2"))
add(x,y)

#Func add 1000 numbers

print("Addition of number",add(1,2,3,4))'''
from functools import reduce

def add(*num):
    return reduce(lambda x,y : x+y , num)

a,b,c = 10,11,13
res=add(a,b,c)
print(res)






