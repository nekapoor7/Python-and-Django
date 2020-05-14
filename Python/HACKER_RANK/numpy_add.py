'''Task

You are given two integer arrays,
and of dimensions X

.
Your task is to perform the following operations:

    Add (

+
)
Subtract (
-
)
Multiply (
*
)
Integer Division (
/
)
Mod (
%
)
Power (
** )'''


import numpy

N,M=map(int,input().split())

a=numpy.array([list(map(int,input().split())) for n in range(N)])
b=numpy.array([list(map(int,input().split())) for n in range(N)])

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
m=a/b

print(numpy.int_(m))
print(numpy.mod(a, b))
print(numpy.power(a, b))
