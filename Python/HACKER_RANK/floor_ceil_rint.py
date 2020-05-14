'''Task
You are given a 1-D array, . Your task is to print the , and of all the elements of . '''

import numpy

Vs = input().split(' ')

arr = numpy.array(Vs, float)

numpy.set_printoptions(sign=' ')

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))