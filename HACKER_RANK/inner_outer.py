'''inner

The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4

outer

The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
'''

import numpy


A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))