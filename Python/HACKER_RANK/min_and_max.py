'''import numpy


A = numpy.array(input().split(), int)
print(A)
print(numpy.min(A, axis=1))'''
'''print(B)
print(type(B))
#print(numpy.array.max(B, axis = None))'''

import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.max(numpy.min(A, axis=1), axis=0))