from legacy import xrange

print(sum(range(1,101)))
print(sum(xrange(1,101)))

print(type(id))

import math
print(math.floor(1.5))
print(math.ceil(1.5))
print(math.trunc(1.5))

print('__code__'.isidentifier())

word = 'abcdefghij'
print(word[:3] + word[3:])

x = 1
print(eval('x+1'))

a = [0,1,2,3,4,5]
list = slice(-3,None)
slice(-3,None,None)
print(a[list])