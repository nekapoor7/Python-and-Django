'''Task

You are given two integer arrays of size
X and X ( & are rows, and is the column). Your task is to concatenate the arrays along axis .'''



import numpy

n,m,p = map(int,input().strip().split())
A = numpy.array([[int(j) for j in input().strip().split()] for i in range(n)])
B = numpy.array([[int(j) for j in input().strip().split()] for i in range(m)])
print(numpy.concatenate((A,B),axis=0))